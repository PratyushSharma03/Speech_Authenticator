# 🔐 Speech Authenticator (with Custom Voice Registration)

A Flask-based web application that enables users to **register with their name and a personalized passphrase**, then **log in using their voice**. The app uses [OpenAI's Whisper model](https://github.com/openai/whisper) to transcribe spoken input and authenticates users by matching the transcript with the stored passphrase. The interface supports both **microphone input** and **file upload**.

---

---

## 🌟 Key Features

- 📝 **User Registration**  
  Register your name along with a custom passphrase securely.

- 🔊 **Voice Login**  
  Authenticate yourself by speaking the exact passphrase you registered with.

- 🧠 **Whisper Model Integration**  
  Utilizes OpenAI's Whisper model to transcribe audio input into text for accurate comparison.

- 🎤 **Mic or File Upload**  
  Choose between recording your passphrase live or uploading an existing audio file.

- 📂 **User Dropdown Menu**  
  Select your registered name from a dynamically generated dropdown list before authentication.

- ❌ **Access Control**  
  If the spoken phrase doesn’t match the registered one, access is denied.

- 👤 **Dynamic Success Screen**  
  Upon successful authentication, the app displays a personalized success message with your name.

---

## 📸 Screenshots

[Speech Authenticator Page](https://drive.google.com/file/d/1LB_VQjHa3bAlfk2OCt4Ke4Wud9vMbLh-/view?usp=sharing)

[Registration Page](https://drive.google.com/file/d/1Ip2PDusQWwkOJCC4XKPyCaBrz7zRxlWl/view?usp=sharing)  

[Access Granted Page](https://drive.google.com/file/d/1p9g4TVqcDaHda2CufuaVPIb-l2ryXcxq/view?usp=sharing)  

---

**Clone this repository**

```bash
git clone https://github.com/your-username/speech-authenticator.git
cd speech-authenticator
  
