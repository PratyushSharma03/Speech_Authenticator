# 🔐 Speech Authenticator (with Custom Voice Registration)

A Flask-based web application that enables users to **register with their name and a personalized passphrase**, then **log in using their voice**. The app uses [OpenAI's Whisper model](https://github.com/openai/whisper) to transcribe spoken input and authenticates users by matching the transcript with the stored passphrase. The interface supports both **microphone input** and **file upload**.

---

## 🌟 Key Features

- 📝 **User Registration**: Register with your name and a custom passphrase.
- 🔊 **Voice Login**: Authenticate by speaking the exact passphrase you registered with.
- 🧠 **Whisper Model Integration**: Transcribes audio input to text for precise comparison.
- 🎤 **Mic or File Upload**: Record your voice directly or upload an existing audio file.
- ❌ **Access Control**: Denies access if the spoken phrase doesn't match any user's registered passphrase.
- 👤 **Dynamic Success Screen**: Displays your name on successful login.

---

## Screenshots

[Speech-Authenticator Page](https://drive.google.com/file/d/1LB_VQjHa3bAlfk2OCt4Ke4Wud9vMbLh-/view?usp=sharing)

[Registration Page](https://drive.google.com/file/d/1Ip2PDusQWwkOJCC4XKPyCaBrz7zRxlWl/view?usp=sharing)  

[Access Granted Page](https://drive.google.com/file/d/1p9g4TVqcDaHda2CufuaVPIb-l2ryXcxq/view?usp=sharing)  

---

1. **Clone this repository**

```bash
git clone https://github.com/your-username/speech-authenticator.git
cd speech-authenticator
  
