# 🌤️ Weather APIs for Tool Calling

Một ứng dụng chatbot thông minh sử dụng **Tool Calling** để tích hợp API thời tiết và gọi hàm động. Ứng dụng cho phép người dùng hỏi thông tin thời tiết theo cách tự nhiên và chatbot sẽ tự động gọi các API phù hợp.

## 📋 Tính Năng

- ✅ **Tool Calling**: Chatbot tự động chọn và gọi đúng function dựa vào yêu cầu người dùng
- 🌍 **Real-time Weather Data**: Lấy thông tin thời tiết thực tế từ OpenWeatherMap API
- 🤖 **Multiple AI Models**: Hỗ trợ Gemini 2.5 Flash Lite và Groq GPT-OSS 120B
- 💬 **Gradio Interface**: Giao diện chat thân thiện và dễ sử dụng
- 🔄 **Smart Tool Iteration**: Xử lý nhiều lần gọi tool (Groq) hoặc một lần gọi (Gemini)

## 🚀 Cách Sử Dụng

### 1. Setup Environment

```bash
# Clone repository
git clone https://github.com/Thangp18/Weather-APIs-for-Tool-Calling.git
cd Weather-APIs-for-Tool-Calling

# Cài đặt dependencies
pip install python-dotenv openai gradio requests
```

### 2. Cấu Hình API Keys

Tạo file `.env` trong thư mục gốc:

```env
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

**Lấy API keys:**
- 🔵 [Google Gemini API](https://ai.google.dev/tutorials/setup)
- ⚫ [Groq API](https://console.groq.com)
- 🌍 [OpenWeatherMap API](https://openweathermap.org/api)

### 3. Chạy Ứng Dụng

Mở notebook `toolcalling.ipynb` và chạy các cell:

```python
# Cell cuối cùng - Basic version
gr.ChatInterface(
    fn=Client,
    title="Chatbot and weatherVN func"
).launch()

# Hoặc chạy Advanced version với model selector
gr.ChatInterface(
    fn=Client_with_model,
    additional_inputs=[
        gr.Dropdown(
            choices=list(models_config.keys()),
            value='Gemini 2.5 Flash Lite',
            label='Chọn Model'
        )
    ],
    title="FlightAI - Weather Assistant"
).launch()
```

## 📸 Gradio Interface

### Version 1: Basic Chatbot
```
┌─────────────────────────────────────┐
│  Chatbot and weatherVN func         │
├─────────────────────────────────────┤
│                                     │
│  User: Thời tiết ở Hà Nội như thế  │
│                                     │
│  Bot: Thời tiết tại Hà Nội hiện    │
│  là 28°C, nhiều mây.               │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ Nhập tin nhắn của bạn...      ▶ │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

### Version 2: Advanced dengan Model Selector
```
┌──────────────────────────────────────────┐
│  FlightAI - Weather Assistant           │
├──────────────────────────────────────────┤
│  Model: ▼ Gemini 2.5 Flash Lite         │
├──────────────────────────────────────────┤
│                                          │
│  User: Thời tiết ở Hồ Chí Minh?        │
│                                          │
│  Bot: Đang lấy dữ liệu thời tiết...    │
│  Thời tiết tại Hồ Chí Minh hiện là     │
│  32°C, nắng.                            │
│                                          │
│ ┌──────────────────────────────────────┐ │
│ │ Nhập tin nhắn của bạn...           ▶ │ │
│ └──────────────────────────────────────┘ │
└──────────────────────────────────────────┘
```

## 🛠️ Kiến Trúc Dự Án

```
├── notebook/
│   ├── toolcalling.ipynb          # Main notebook
│   ├── attn.ipynb                 # Attention mechanisms
│   ├── multiheadAttn.ipynb        # Multi-head attention
│   ├── casualAttn.ipynb           # Causal attention
│   ├── bpe.ipynb                  # Byte pair encoding
│   ├── dataset.ipynb              # Dataset processing
│   ├── hgface.ipynb               # HuggingFace integration
│   └── LLMTokenizer.ipynb         # Tokenizer
├── data/
│   └── gradientdescent.txt        # Reference data
├── .env                            # API keys (not in repo)
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## 💡 Cách Hoạt Động

### Tool Calling Flow

```
1. User: "Hôm nay thời tiết ở Đà Nẵng thế nào?"
                          ↓
2. LLM Analysis: Câu hỏi về thời tiết → cần gọi get_weather_infor()
                          ↓
3. Tool Call: get_weather_infor("Đà Nẵng")
                          ↓
4. API Request: https://api.openweathermap.org/data/2.5/weather?q=Da%20Nang...
                          ↓
5. Response: {"temp": 30, "description": "Nắng"}
                          ↓
6. Bot Reply: "Thời tiết tại Đà Nẵng hiện là 30°C, nắng."
```

## 🔧 Các Tools/Functions Có Sẵn

### 1. **get_weather_infor(destination_city)**
Lấy thông tin thời tiết theo tên thành phố
```python
# Example
get_weather_infor("HaNoi")
# Output: "Thời tiết tại HaNoi hiện là 28°C, nhiều mây."
```

## 📊 Hỗ Trợ Models

| Model | Base | Max Iterations | Độ Trễ | Chi Phí |
|-------|------|----------------|--------|---------|
| Gemini 2.5 Flash Lite | Google | 1 | Thấp | Rẻ |
| Groq GPT-OSS 120B | Groq | 5 | Rất Thấp | Miễn phí |

## 🐛 Troubleshooting

### Lỗi `.env` không được tải
**Giải pháp:**
```python
from dotenv import load_dotenv
load_dotenv(r'd:\AI\Deeplearning\BuildLLMs\.env', override=True)
```

### API Key không hợp lệ
- Kiểm tra file `.env` có đúng format không
- Xác nhận API keys còn hiệu lực
- Đảm bảo API keys có quyền sử dụng

### Gradio không hiển thị
```bash
pip install --upgrade gradio
```

## 📝 Requirements

```
python-dotenv>=1.0.0
openai>=1.3.0
gradio>=4.0.0
requests>=2.31.0
```

## 📄 License

MIT License - Tự do sử dụng cho mục đích học tập

## 👨‍💻 Author

**Thang Pham** - [@Thangp18](https://github.com/Thangp18)

## 🤝 Contribute

Pull requests are welcome! Vui lòng tạo issue trước khi submit PR.

---

**⭐ Nếu bạn thấy dự án hữu ích, vui lòng star repository!**
