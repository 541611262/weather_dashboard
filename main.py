import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import weather_plots as wp  # 保持原有模块引用不变
from fetch_data import fetch_weather_data
from process_data import process_weather_data

# 配置全局matplotlib样式
plt.rcParams.update({
    'font.size': 8,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 100,
    'figure.autolayout': True
})


def determine_weather(row, sunny_threshold=25, rainy_min_temp_threshold=15, rainy_humidity_threshold=80):
    """天气判断函数保持不变"""
    if row['Max Temperature (C)'] > sunny_threshold:
        return 'Sunny'
    elif (row['Min Temperature (C)'] < rainy_min_temp_threshold and
          row['Max Humidity (%)'] > rainy_humidity_threshold):
        return 'Rainy'
    else:
        return 'Partly Cloudy'


def update_weather():
    """更新天气数据并绘制图表"""
    city = city_var.get()
    api_key = '038f75ef1dc83b9268d105fbcde93b9a'  # 建议使用环境变量

    # 更新加载状态
    loading_label.config(text="Fetching weather data...", foreground="#2196F3")
    root.update()

    try:
        current_data, forecast_data = fetch_weather_data(api_key, city)
        if current_data is None or forecast_data is None:
            raise ValueError("Empty data received")

        loading_label.config(text="Processing data...", foreground="#2196F3")
        root.update()

        current_df, hourly_df, daily_df = process_weather_data(current_data, forecast_data)

        # 处理每日数据
        if daily_df is not None:
            daily_df['Weather'] = daily_df.apply(determine_weather, axis=1)
            daily_df['Max Temperature (C)'] = daily_df['Max Temperature (C)'].round(2)
            daily_df['Min Temperature (C)'] = daily_df['Min Temperature (C)'].round(2)

        # 清除旧图表
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # 准备绘图数据
        x_ticks = hourly_df['Datetime'][::6]

        # 创建图表
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.subplots_adjust(hspace=0.5, wspace=0.4)

        # 温度曲线图
        axs[0, 0].plot(hourly_df['Datetime'], hourly_df['Temperature (C)'],
                       marker='o', markersize=4, linewidth=1, color='#FF5722')
        axs[0, 0].set_title('Temperature Trend', pad=12, fontweight='bold')
        axs[0, 0].set_xticks(x_ticks)
        axs[0, 0].tick_params(axis='x', rotation=30)

        # 添加趋势线
        x_num = hourly_df['Datetime'].astype(np.int64) // 10 ** 9
        coeff = np.polyfit(x_num, hourly_df['Temperature (C)'], 1)
        axs[0, 0].plot(hourly_df['Datetime'], np.polyval(coeff, x_num),
                       '--', color='#9E9E9E')

        # 湿度柱状图
        bars = axs[0, 1].bar(hourly_df['Datetime'], hourly_df['Humidity (%)'],
                             width=0.05, color='#4CAF50', alpha=0.8)
        axs[0, 1].set_title('Humidity Distribution', pad=12, fontweight='bold')
        axs[0, 1].set_ylim(0, 100)
        axs[0, 1].set_xticks(x_ticks)
        axs[0, 1].tick_params(axis='x', rotation=45)  # 横坐标倾斜45度

        # 天气饼图
        weather_counts = hourly_df['Weather'].value_counts()
        wedges, texts, autotexts = axs[1, 0].pie(
            weather_counts,
            labels=weather_counts.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=['#FFC107', '#2196F3', '#4CAF50'],
            textprops={'fontsize': 7},
            radius=1.2  # 增大饼图大小
        )
        axs[1, 0].set_title('Weather Composition', pad=12, fontweight='bold')

        # 风速散点图
        scatter = axs[1, 1].scatter(
            hourly_df['Temperature (C)'],
            hourly_df['Wind Speed (m/s)'],
            c=hourly_df['Humidity (%)'],
            cmap='Blues',
            s=40,
            alpha=0.7
        )
        axs[1, 1].set_title('Temperature vs Wind Speed', pad=12, fontweight='bold')
        plt.colorbar(scatter, ax=axs[1, 1]).set_label('Humidity (%)')

        # 统一图表样式
        for ax in axs.flat:
            ax.grid(alpha=0.2)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

        # 嵌入图表到界面
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        loading_label.config(text=f"Data updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
                             foreground="#4CAF50")

    except Exception as e:
        loading_label.config(text=f"Error: {str(e)}", foreground="#f44336")
        messagebox.showerror("Error",
                             f"Failed to update data:\n{str(e)}\nPlease check network connection or city name.")
        print(f"Error occurred: {str(e)}")


# 初始化主窗口
root = tk.Tk()
root.title("Advanced Weather Dashboard")
root.geometry("1280x800")
root.configure(bg='#ffffff')

# 配置现代风格
style = ttk.Style()
style.theme_use('clam')

# 定义全局样式
font_settings = ('Segoe UI', 10)
style.configure("TButton",
                font=font_settings,
                padding=8,
                relief="flat",
                background="#2196F3",
                foreground="white")
style.map("TButton",
          background=[('active', '#1976D2')],
          foreground=[('active', 'white')])

style.configure("TCombobox",
                font=font_settings,
                padding=6,
                fieldbackground="#ffffff")

style.configure("TLabel",
                font=font_settings,
                background="#ffffff",
                foreground="#212121")

style.configure("Header.TLabel",
                font=("Segoe UI", 16, "bold"),
                foreground="#2c3e50")

# 创建界面框架
header_frame = ttk.Frame(root, padding=(20, 15, 20, 10))
header_frame.pack(fill=tk.X)

control_frame = ttk.Frame(root, padding=(20, 10))
control_frame.pack(fill=tk.X)

plot_frame = ttk.Frame(root)
plot_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=(0, 20))

# 标题区域
title_label = ttk.Label(header_frame,
                        text="🌤 Weather Analytics Dashboard",
                        style="Header.TLabel")
title_label.pack(side=tk.LEFT)

# 控制面板
input_frame = ttk.Frame(control_frame)
input_frame.pack()

# 城市选择
city_var = tk.StringVar(value='Sydney')
ttk.Label(input_frame, text="Select City:").grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
city_dropdown = ttk.Combobox(
    input_frame,
    textvariable=city_var,
    values=['Sydney', 'New York', 'London', 'Tokyo', 'Beijing', 'Paris'],
    width=22,
    state='normal'
)
city_dropdown.grid(row=0, column=1, padx=5, pady=2)

# 更新按钮
update_btn = ttk.Button(
    input_frame,
    text="🔄 Refresh Data",
    command=update_weather,
    width=15
)
update_btn.grid(row=0, column=2, padx=10, pady=2)

# 状态标签
loading_label = ttk.Label(control_frame,
                          text="Ready to fetch data...",
                          foreground="#757575")
loading_label.pack(pady=(5, 0))

# 响应式布局配置
plot_frame.columnconfigure(0, weight=1)
plot_frame.rowconfigure(0, weight=1)

# 初始化数据
update_weather()

# 启动主循环
root.mainloop()