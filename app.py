import asyncio
from datetime import datetime

import streamlit as st
from core.pipeline import pipeline
from database.session import session_mgr
from utils.logger import setup_logging

setup_logging()

# 页面配置
import streamlit as st

st.set_page_config(
    page_title="AgenticAI v1.0",
    page_icon="🤖",
    layout="wide"
)

# ============ 终极无白边版本 ============
st.markdown("""<style>
/* 深色模式样式 */
@media (prefers-color-scheme: dark) {
    /* ===== 第1层：最外层容器 ===== */
    html, body {
        background-color: #0E1117 !important;
    }
    
    /* ===== 第2层：Streamlit 主容器 ===== */
    .stApp,
    [data-testid="stAppViewContainer"],
    [class*="appview"] {
        background-color: #0E1117 !important;
    }
    
    /* ===== 第3层：主内容区域 ===== */
    section[data-testid="stMain"],
    section[data-testid="stMain"] > div,
    section[data-testid="stMain"] > div > div,
    .main,
    .main > div,
    .main > div > div {
        background-color: #0E1117 !important;
    }
    
    /* ===== 第4层：Block 容器 ===== */
    .block-container,
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"],
    .element-container {
        background-color: #0E1117 !important;
    }
    
    /* ===== 侧边栏 ===== */
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > div,
    section[data-testid="stSidebar"] * {
        background-color: #262730 !important;
    }
    
    /* ===== 聊天消息：强力去白边 ===== */
    /* 聊天消息的所有父容器 */
    [data-testid="stChatMessageContainer"],
    [data-testid="stChatMessageContainer"] > div,
    [data-testid="stChatMessageContainer"] > div > div,
    .stChatMessageContainer,
    [class*="ChatMessageContainer"],
    [class*="chatMessage"] {
        background-color: #0E1117 !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* 聊天消息框本身 */
    .stChatMessage,
    [class*="ChatMessage"],
    [data-testid="chat-message"] {
        background-color: #262730 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 15px !important;
        margin: 10px 0 !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    /* 用户消息 */
    .stChatMessage[data-testid="user-message"],
    [data-testid="user-message"] {
        background-color: #1E293B !important;
    }
    
    /* 助手消息 */
    .stChatMessage[data-testid="assistant-message"],
    [data-testid="assistant-message"] {
        background-color: #262730 !important;
    }
    
    /* 聊天消息内部的所有容器 */
    .stChatMessage > div,
    .stChatMessage > div > div,
    .stChatMessage * {
        background-color: transparent !important;
        border: none !important;
    }
    
    /* ===== 聊天输入框 ===== */
    .stChatInputContainer,
    [data-testid="stChatInputContainer"],
    [data-testid="stChatInputContainer"] > div {
        background-color: #0E1117 !important;
        border: none !important;
    }
    
    .stChatInput,
    .stChatInput > div {
        background-color: #262730 !important;
        border: 1px solid #374151 !important;
        border-radius: 10px !important;
    }
    
    .stChatInput textarea {
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border: none !important;
    }
    
    /* ===== 通用输入组件 ===== */
    input, textarea, select {
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border: 1px solid #374151 !important;
    }
    
    /* ===== 按钮 ===== */
    .stButton button {
        background-color: #8B5CF6 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }
    
    .stButton button:hover {
        background-color: #7C3AED !important;
    }
    
    /* ===== 代码块 ===== */
    code, pre {
        background-color: #1E293B !important;
        color: #E2E8F0 !important;
        border: 1px solid #374151 !important;
    }
    
    /* ===== 文字颜色 ===== */
    p, span, label, div, h1, h2, h3, h4, h5, h6 {
        color: #FAFAFA !important;
    }
    
    /* Markdown */
    .stMarkdown {
        color: #FAFAFA !important;
    }
    
    .stMarkdown a {
        color: #8B5CF6 !important;
    }
    
    /* ===== 强制移除所有可能的白色背景 ===== */
    div[style*="background-color: white"],
    div[style*="background-color: rgb(255, 255, 255)"],
    div[style*="background-color: #fff"],
    div[style*="background-color: #ffffff"] {
        background-color: #0E1117 !important;
    }
    
    /* ===== Header 和 Toolbar ===== */
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        background-color: #0E1117 !important;
    }
    
    /* ===== 滚动条 ===== */
    ::-webkit-scrollbar {
        width: 10px;
        background: #0E1117;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #4B5563;
        border-radius: 5px;
    }
    
    /* ===== 展开器 ===== */
    .streamlit-expanderHeader {
        background-color: #262730 !important;
        border: none !important;
    }
    
    .streamlit-expanderContent {
        background-color: #1E293B !important;
        border: none !important;
    }
}
</style>""", unsafe_allow_html=True)
# ==========================================

# 自定义 CSS 样式
st.markdown("""
<style>
    /* 导入 Google Fonts - 使用更现代的字体组合 */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:wght@700&display=swap');
    
    /* 全局变量 */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --surface: #ffffff;
        --surface-alt: #f8f9fa;
        --border: #e2e8f0;
        --text-primary: #1a202c;
        --text-secondary: #718096;
        --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
        --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
    }
    
    /* 重置 Streamlit 默认样式 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* 隐藏 Streamlit 默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    #header {visibility: hidden;}
    
    /* 主容器 */
    .block-container {
        padding: 2rem 3rem 3rem 3rem;
        max-width: 1400px;
    }
    
    /* 标题区域 */
    .main-header {
        background: var(--surface);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-md);
        border: 1px solid var(--border);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--primary-gradient);
    }
    
    .header-content {
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }
    
    .header-icon {
        width: 56px;
        height: 56px;
        background: var(--primary-gradient);
        border-radius: var(--radius-md);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        box-shadow: var(--shadow-md);
    }
    
    .header-text h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.2;
    }
    
    .header-text p {
        color: var(--text-secondary);
        font-size: 0.95rem;
        margin: 0.25rem 0 0 0;
        font-weight: 500;
    }
    
    /* 聊天容器 */
    .chat-container {
        background: var(--surface);
        border-radius: var(--radius-lg);
        padding: 2rem;
        box-shadow: var(--shadow-md);
        border: 1px solid var(--border);
        min-height: 500px;
        max-height: 650px;
        overflow-y: auto;
        margin-bottom: 1.5rem;
    }
    
    /* 自定义滚动条 */
    .chat-container::-webkit-scrollbar {
        width: 8px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: var(--surface-alt);
        border-radius: 4px;
    }
    
    .chat-container::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        border-radius: 4px;
    }
    
    /* 消息样式 */
    .stChatMessage {
        background: transparent !important;
        padding: 1rem 0 !important;
        border-radius: 0 !important;
    }
    
    [data-testid="stChatMessageContent"] {
        background: var(--surface-alt);
        border-radius: var(--radius-md);
        padding: 1rem 1.25rem;
        border: 1px solid var(--border);
        box-shadow: var(--shadow-sm);
    }
    
    /* 用户消息 */
    .stChatMessage[data-testid*="user"] [data-testid="stChatMessageContent"] {
        background: var(--primary-gradient);
        color: white;
        border: none;
        margin-left: auto;
        max-width: 85%;
        box-shadow: var(--shadow-md);
    }
    
    /* 助手消息 */
    .stChatMessage[data-testid*="assistant"] [data-testid="stChatMessageContent"] {
        background: var(--surface);
        border: 1px solid var(--border);
        max-width: 92%;
    }
    
    /* 输入框样式 */
    .stChatInputContainer {
        border: none !important;
        background: var(--surface) !important;
        border-radius: var(--radius-lg) !important;
        box-shadow: var(--shadow-md) !important;
        padding: 0.5rem !important;
        border: 2px solid var(--border) !important;
        transition: all 0.3s ease;
    }
    
    .stChatInputContainer:focus-within {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1), var(--shadow-md) !important;
    }
    
    .stChatInput textarea {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        color: var(--text-primary) !important;
    }
    
    /* 状态指示器 */
    .status-indicator {
        background: var(--surface);
        border-radius: var(--radius-md);
        padding: 1rem 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid var(--border);
        box-shadow: var(--shadow-sm);
        display: flex;
        align-items: center;
        gap: 0.75rem;
        animation: slideIn 0.3s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .status-indicator.info {
        background: linear-gradient(135deg, #e0f2fe 0%, #dbeafe 100%);
        border-color: #93c5fd;
        color: #1e40af;
    }
    
    .status-indicator.success {
        background: linear-gradient(135deg, #d1fae5 0%, #d1f4e0 100%);
        border-color: #86efac;
        color: #065f46;
    }
    
    .status-indicator.error {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-color: #fca5a5;
        color: #991b1b;
    }
    
    .status-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Expander 样式 */
    .streamlit-expanderHeader {
        background: var(--surface-alt) !important;
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--border) !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        padding: 0.875rem 1.25rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: var(--surface) !important;
        border-color: #667eea !important;
    }
    
    .streamlit-expanderContent {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-top: none !important;
        border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
        padding: 1.25rem !important;
    }
    
    /* Metric 样式 */
    [data-testid="stMetric"] {
        background: var(--surface-alt);
        padding: 1rem;
        border-radius: var(--radius-md);
        border: 1px solid var(--border);
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary);
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stMetricValue"] {
        color: var(--text-primary);
        font-size: 1.5rem;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* 代码块样式 */
    code {
        font-family: 'JetBrains Mono', monospace !important;
        background: #1e1e1e !important;
        color: #d4d4d4 !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 4px !important;
        font-size: 0.875rem !important;
    }
    
    pre {
        background: #1e1e1e !important;
        border-radius: var(--radius-md) !important;
        border: 1px solid #2d2d2d !important;
        box-shadow: var(--shadow-sm) !important;
    }
    
    /* 侧边栏样式 */
    [data-testid="stSidebar"] {
        background: var(--surface) !important;
        border-right: 1px solid var(--border) !important;
    }
    
    /* 隐藏语言选择框 */
    [data-testid="stSidebar"] div[data-testid="stSelectbox"]:has(label:contains("语言")) {
        display: none !important;
    }

    [data-testid="stSidebar"] .block-container {
        padding: 1.5rem 1rem !important;
    }

    
    /* 按钮样式 */
    .stButton button {
        background: var(--primary-gradient);
        color: white;
        border: none;
        border-radius: var(--radius-md);
        padding: 0.625rem 1.25rem;
        font-weight: 600;
        font-size: 0.9rem;
        box-shadow: var(--shadow-sm);
        transition: all 0.2s ease;
        font-family: 'DM Sans', sans-serif;
    }
    
    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: var(--shadow-md);
    }
    
    /* 复选框样式 */
    .stCheckbox {
        padding: 0.5rem 0;
    }
    
    /* JSON 样式 */
    .stJson {
        background: var(--surface-alt) !important;
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--border) !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* 响应式设计 */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }
        
        .main-header {
            padding: 1.5rem;
        }
        
        .header-content {
            flex-direction: column;
            text-align: center;
        }
    }
    
    /* 加载动画 */
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    .loading-shimmer {
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 1000px 100%;
        animation: shimmer 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# 主标题
st.markdown("""
<div class="main-header">
    <div class="header-content">
        <div class="header-icon">🤖</div>
        <div class="header-text">
            <h1>AgenticAI v1.0</h1>
            <p>一个基于 LangGraph 的多智能体协作系统，支持 Web 搜索和深度思考，带有会话记忆和流式输出功能的系统 </p>
            <p>LangGraph Multi-Agent System: Web-enhanced, deep-reasoning AI with contextual memory and real-time streaming.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    
    #st.markdown("### ⚙️ System Info")    
    # 隐藏语言选择框，使用固定默认语言
    language = "中文"  # 默认语言
    
    #st.divider()
    
    st.markdown("### 🎯 Processing Options")
    
    enable_deep_thinking = st.checkbox(
        "🧠 Deep Thinking Mode",
        value=False,
        help="Chain-of-Thought (CoT) Reasoning"
    )
    
    enable_web_search = st.checkbox(
        "🌐 Web Search",
        value=False,
        help="Real-time Web Retrieval (Tavily)"
    )
    
    with st.expander("ℹ️ Workflow Description", expanded=False):
        st.markdown("""
        **Basic Mode:**          
        Understanding → Analysis → Response
        
        **Deep Thinking:**          
        Self-reflection and Optimization
                    
        **Web Search:**          
        Real-time Information Retrieval
                    
        **Medical / Legal:**          
        Automatically enables Web Search
                    
        **Architecture / Development:**          
        Automatically enables Code Generation
        """)
    
    st.divider()
    
    st.markdown("### 📚 Session Management")
    
    if st.button("➕ New Session", use_container_width=True):
        new_session_id = session_mgr.create_session(
            f"会话 {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "general",
            language,
        )
        st.session_state.current_session = new_session_id
        st.session_state.messages = []
        st.rerun()
    
    sessions = session_mgr.list_sessions()
    
    if sessions:
        session_options = {}
        for s in sessions:
            session_id = s["session_id"]
            summary = s.get("summary", "").strip()
            
            if not summary:
                messages = session_mgr.get_messages(session_id, limit=1)
                if messages and messages[0]["role"] == "user":
                    first_msg = messages[0]["content"]
                    summary = first_msg[:40] + "..." if len(first_msg) > 40 else first_msg
                else:
                    summary = "(New Chat)"
            
            updated_time = datetime.fromtimestamp(s["updated_at"])
            today = datetime.now().date()
            
            if updated_time.date() == today:
                time_str = updated_time.strftime("%H:%M")
            else:
                time_str = updated_time.strftime("%m-%d")
            
            display_text = f"💬 {summary}\n📅 {time_str} · {s.get('domain', 'general')}"
            session_options[session_id] = display_text
        
        # 如果当前没有选中的会话，则自动选择最新的会话
        if "current_session" not in st.session_state or st.session_state.current_session not in session_options:
            st.session_state.current_session = list(session_options.keys())[0]
        
        selected = st.selectbox(
            "选择会话",
            options=list(session_options.keys()),
            format_func=lambda x: session_options.get(x, "Unknown"),
            index=list(session_options.keys()).index(st.session_state.current_session) if st.session_state.current_session in session_options else 0,
            key="session_selector",
            label_visibility="collapsed"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📂 Load", use_container_width=True):
                if selected and selected != st.session_state.get("current_session"):
                    st.session_state.current_session = selected
                    history = session_mgr.get_messages(selected)
                    st.session_state.messages = [
                        {"role": msg["role"], "content": msg["content"]}
                        for msg in history
                    ]
                    st.rerun()
        
        with col2:
            if st.button("🗑️ Delete", use_container_width=True):
                if selected:
                    confirm_key = f"confirm_delete_{selected}"
                    if not st.session_state.get(confirm_key, False):
                        st.session_state[confirm_key] = True
                        st.warning("⚠️ 再次点击确认删除")
                    else:
                        session_mgr.delete_session(selected)
                        st.session_state[confirm_key] = False
                        
                        if selected == st.session_state.get("current_session"):
                            # 删除当前会话后，清空会话状态，不自动创建新会话
                            st.session_state.pop("current_session", None)
                            st.session_state.messages = []
                        
                        st.success("✅ 会话已删除")
                        st.rerun()
    
    st.divider()
    
    with st.expander("🗂️ Deleted Sessions (Audit)", expanded=False):
        deleted_sessions = session_mgr.list_sessions(status="deleted")
        if deleted_sessions:
            st.caption(f"共 {len(deleted_sessions)} 个已删除会话")
            for s in deleted_sessions[:5]:
                deleted_time = datetime.fromtimestamp(s["updated_at"]).strftime("%Y-%m-%d %H:%M")
                summary = s.get("summary", "无摘要")[:30]
                st.text(f"🗑️ {summary}")
                st.caption(f"   {deleted_time} · {s.get('domain', 'N/A')}")
        else:
            st.caption("暂无已删除会话")

# 初始化会话 - 修改逻辑：不自动创建，而是从现有会话中加载最新的
if "current_session" not in st.session_state:
    # 获取所有现有会话
    existing_sessions = session_mgr.list_sessions()
    if existing_sessions:
        # 如果有现有会话，自动加载最新的（第一个）
        latest_session = existing_sessions[0]["session_id"]
        st.session_state.current_session = latest_session
        # 加载该会话的历史消息
        history = session_mgr.get_messages(latest_session)
        st.session_state.messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in history
        ]
    else:
        # 如果没有任何会话，不创建，等待用户手动创建
        st.session_state.messages = []

# 如果没有当前会话，显示提示信息
if "current_session" not in st.session_state or not st.session_state.current_session:
    st.info("👋 欢迎使用 AgenticAI！请点击左侧 **➕ 新建会话** 开始对话。")
else:
    # 如果 messages 未初始化，加载当前会话的历史
    if "messages" not in st.session_state:
        history = session_mgr.get_messages(st.session_state.current_session)
        st.session_state.messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in history
        ]
    
    # 显示聊天历史
    with st.container():
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # 聊天输入
    if prompt := st.chat_input("💭 输入你的问题...", key="chat_input"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            status_placeholder = st.empty()
            content_placeholder = st.empty()
            
            async def process_streaming():
                full_response = ""
                metadata = {}
                
                try:
                    async for event in pipeline.run_streaming(
                        query=prompt,
                        session_id=st.session_state.current_session,
                        language=language,
                        enable_deep_thinking=enable_deep_thinking,
                        enable_web_search=enable_web_search,
                    ):
                        event_type = event.get("type")
                        content = event.get("content", "")
                        
                        if event_type == "status":
                            # 显示状态更新（使用自定义样式）
                            step = event.get("step", "")
                            status_class = "info"
                            
                            if "complete" in step:
                                status_class = "success"
                            elif "error" in step:
                                status_class = "error"
                            
                            status_placeholder.markdown(
                                f'<div class="status-indicator {status_class}">'
                                f'<div class="status-icon">⚡</div>'
                                f'<div>{content}</div>'
                                f'</div>',
                                unsafe_allow_html=True
                            )
                        
                        elif event_type == "content":
                            full_response += content
                            content_placeholder.markdown(full_response + "▌")
                        
                        elif event_type == "final":
                            full_response = content
                            metadata = event.get("metadata", {})
                            status_placeholder.empty()
                            content_placeholder.markdown(full_response)
                        
                        elif event_type == "error":
                            status_placeholder.markdown(
                                f'<div class="status-indicator error">'
                                f'<div class="status-icon">❌</div>'
                                f'<div>{content}</div>'
                                f'</div>',
                                unsafe_allow_html=True
                            )
                            return None, None
                    
                    return full_response, metadata
                
                except Exception as e:
                    status_placeholder.markdown(
                        f'<div class="status-indicator error">'
                        f'<div class="status-icon">❌</div>'
                        f'<div>处理出错: {str(e)}</div>'
                        f'</div>',
                        unsafe_allow_html=True
                    )
                    return None, None
            
            result = asyncio.run(process_streaming())
            
            if result[0]:
                full_response, metadata = result
                
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )
                
                if metadata:
                    with st.expander("📊 执行详情", expanded=False):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("⏱️ 执行时间", f"{metadata.get('elapsed', 0):.2f}s")
                        with col2:
                            st.metric("📦 生成文件", len(metadata.get("artifacts", [])))
                        
                        if metadata.get("understanding"):
                            st.markdown("#### 🎯 需求理解")
                            st.json(
                                metadata["understanding"].dict()
                                if hasattr(metadata["understanding"], "dict")
                                else metadata["understanding"]
                            )