User Guide (使用说明)
1. Environment Preparation (环境准备)
Install Dependencies (安装依赖库)
Before running the program, ensure that the following Python libraries are installed:
pip install pandas matplotlib tkinter requests numpy

2. Obtain OpenWeatherMap API Key (获取OpenWeatherMap API密钥)
Visit the OpenWeatherMap website(https://openweathermap.org) and register an account.
Generate an API key (the free version is sufficient).
Replace the default API key:
Open main.py, find the following line:
api_key = '038f75ef1dc83b9268d105fbcde93b9a'  # It is recommended to use an environment variable

Replace '038f75ef1dc83b9268d105fbcde93b9a' with your own API key.
3. Run the Program (运行程序)
Execute the following command to start the weather dashboard:
python main.py

4. Interface Operation Guide (界面操作指南)
Select City (选择城市):
The default city is Sydney, and the following cities are supported:
Sydney, New York, London, Tokyo, Beijing, Paris.
You can select another city from the drop-down menu or enter the city name yourself.
Refresh Data (刷新数据):
Click the 🔄 Refresh Data button to retrieve the latest weather data in real-time.
Graph Display (图表展示):

Temperature Trend Graph (温度趋势图): Displays temperature changes over the next few hours with a trend line.
Humidity Distribution Graph (湿度分布图): Displays hourly humidity percentage.
Weather Composition Pie Chart (天气组成饼图): Shows the proportion of current weather types (e.g., sunny, rainy).
Temperature vs Wind Speed Scatter Plot (温度 vs 风速散点图): A scatter plot showing the relationship between temperature and wind speed, incorporating humidity data.

5. Generated Data Files (生成的数据文件)
The program will automatically generate the following CSV files:

current_weather_data.csv: Current weather data.
hourly_weather_data.csv: Hourly forecast data.
daily_weather_stats.csv: Daily statistics (high/low temperatures, humidity, wind speed).

6. Notes (注意事项)

API Call Limit (API调用限制):
The free version of OpenWeatherMap has an API call frequency limit (60 times per minute). Frequent refreshing may lead to temporary suspension.
Network Requirements (网络要求):
The program requires a stable internet connection to fetch real-time data. If errors occur, check your network connection or the spelling of the city name.
Compatibility (兼容性):
Supports Python version 3.7 and above.
If there are display issues, ensure your system supports Chinese character sets (check for encoding problems).

7.FAQ (常见问题)

Q1: Graphs not updating or displaying blank (图表未更新或显示空白)  
Check if your API key is correct.  
Confirm that the selected city is in OpenWeatherMap's supported list.
Q2: Program throws ModuleNotFoundError (程序报错 ModuleNotFoundError)  
Ensure all required libraries (such as requests, pandas, etc.) are installed correctly.
Q3: Data delay (数据延迟)  
The free version of OpenWeatherMap updates less frequently, so some forecast data might be delayed.


用户指南
1. 环境准备
安装依赖库
在运行程序前，请确保已安装以下Python库：
pip install requests pandas matplotlib tkinter

2. 获取OpenWeatherMap API密钥
访问OpenWeatherMap官网(https://openweathermap.org)并注册账号。
生成一个API密钥（免费版即可）。
替换默认密钥：
打开main.py，找到以下行：
api_key = '038f75ef1dc83b9268d105fbcde93b9a'  # 建议使用环境变量

将 '038f75ef1dc83b9268d105fbcde93b9a' 替换为您自己的API密钥。
3. 运行程序
执行以下命令启动天气仪表盘：
python main.py

4. 界面操作指南
选择城市：
默认城市为Sydney，支持以下城市：
Sydney、New York、London、Tokyo、Beijing、Paris。
可以通过下拉菜单选择其他城市或者自己输入城市名称。
刷新数据：
点击🔄 Refresh Data按钮，实时获取最新天气数据。
图表展示：

温度趋势图： 显示未来几小时的温度变化及趋势线。
湿度分布图： 按小时展示湿度百分比。
天气组成饼图： 当前天气类型（晴天、雨天等）的占比。
温度 vs 风速散点图： 结合湿度信息的温度与风速关系图。

5. 生成的数据文件
程序会自动生成以下CSV文件：

current_weather_data.csv：当前天气数据。
hourly_weather_data.csv：逐小时预报数据。
daily_weather_stats.csv：每日统计（最高/最低温度、湿度、风速）。

6. 注意事项
API调用限制：
OpenWeatherMap免费版有API调用频率限制（60次/分钟），频繁刷新可能导致临时封禁。
网络要求：
程序需要稳定的网络连接以获取实时数据，若出现错误请检查网络或城市名称拼写。
兼容性：
支持Python 3.7及以上版本。
若界面显示异常，请确保系统支持中文字符集（如遇编码问题）。

7. 常见问题

Q1：图表未更新或显示空白  
检查API密钥是否正确。  
确认所选城市在OpenWeatherMap支持列表中。
Q2：程序报错ModuleNotFoundError  
确保所有依赖库已正确安装（如requests, pandas等）。
Q3：数据延迟  
OpenWeatherMap免费版数据更新频率较低，部分预报数据可能存在延迟。
