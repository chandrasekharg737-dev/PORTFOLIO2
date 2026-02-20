document.addEventListener('DOMContentLoaded', () => {
    // Add interaction logic here if needed
    console.log('Dashboard loaded');

    // Add active class to nav items
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            // Remove active from all
            document.querySelectorAll('.nav-links li').forEach(li => li.classList.remove('active'));
            // Add to parent li
            this.parentElement.classList.add('active');
        });
    });

    // Mobile Menu Toggle
    const menuToggle = document.getElementById('mobile-menu');
    const sidebar = document.querySelector('.sidebar');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            sidebar.classList.toggle('active');
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
            if (!sidebar.contains(e.target) && !menuToggle.contains(e.target) && sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
            }
        }
    });

    // Chatbot functionality
    const chatToggle = document.getElementById('chat-toggle');
    const chatWindow = document.getElementById('chat-window');
    const chatClose = document.getElementById('chat-close');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    const chatMessages = document.getElementById('chat-messages');

    if (chatToggle && chatWindow && chatClose) {
        chatToggle.addEventListener('click', () => {
            chatWindow.classList.toggle('hidden');
        });

        chatClose.addEventListener('click', () => {
            chatWindow.classList.add('hidden');
        });
    }

    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';

        // Add loading indicator
        const loadingId = addMessage('Thinking...', 'bot');

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();

            // Remove loading and add bot response
            const loadingMsg = document.querySelector(`[data-id="${loadingId}"]`);
            if (loadingMsg) loadingMsg.remove();

            if (data.error) {
                addMessage('Sorry, something went wrong.', 'bot');
            } else {
                addMessage(data.response, 'bot');
            }
        } catch (error) {
            console.error('Error:', error);
            const loadingMsg = document.querySelector(`[data-id="${loadingId}"]`);
            if (loadingMsg) loadingMsg.remove();
            addMessage('Error connecting to server.', 'bot');
        }
    }

    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message', sender);

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = text;

        msgDiv.appendChild(contentDiv);

        const id = Date.now().toString();
        msgDiv.setAttribute('data-id', id);

        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        return id;
    }

    if (chatSend && chatInput) {
        chatSend.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
});
