# Raznet RealTalk

Raznet RealTalk is a modern real-time chat application available as both a **web interface** and an **Android app**. It supports real-time chat functionality, user authentication, and seamless navigation between multiple screens.

## 📱 Features (Android Version)
- **User Authentication**: Secure login and signup using Firebase Authentication.
- **Real-Time Navigation**: Smooth navigation between screens (Login, Home, Chat, Profile) powered by Jetpack Compose.
- **Responsive UI**: Built with Material Design 3 components for a clean and intuitive user experience.
- **Modular Architecture**: Organized and maintainable code structure with separate files for each screen.
- **Firebase Integration**: Real-time database functionality integrated with Firebase services.

## 🌐 Features (Web Version)
- **Responsive Design**: Clean and modern UI built with HTML, CSS, and JavaScript to support mobile and desktop browsers.
- **Navigation System**: Includes login, home, chat, and profile screens, similar to the Android app.
- **Lightweight Framework**: Fully responsive using pure HTML, CSS, and JavaScript without requiring external libraries.
- **Expandable Architecture**: Designed to integrate with Firebase for future real-time chat functionality.

## 🛠️ Tech Stack
### Frontend (Android):
- **Jetpack Compose**: Modern declarative UI toolkit for Android.
- **Material Design 3**: Ensures responsive and attractive interfaces.

### Frontend (Web):
- **HTML5**: Semantic markup for a clean structure.
- **CSS3**: Responsive and modern styling with intuitive layouts.
- **JavaScript (ES6)**: Interactive navigation and dynamic behavior.

### Backend:
- **Firebase Authentication**: Handles user login and registration.
- **Firebase Realtime Database**: (Planned) For real-time chat and message synchronization.

## 📂 Project Structure

### Android


RaznetRealTalk/ ├── app/ │ ├── src/ │ │ ├── main/ │ │ │ ├── kotlin/com/example/raznetrealtalkapp/ │ │ │ │ ├── MainActivity.kt │ │ │ │ ├── LoginScreen.kt │ │ │ │ ├── GreetingScreen.kt │ │ │ │ ├── ChatScreen.kt │ │ │ │ ├── ProfileScreen.kt │ │ │ ├── AndroidManifest.xml │ ├── build.gradle.kts ├── build.gradle.kts ├── .gitignore


### Web Interface

RaznetRealTalk/ ├── app/ │ ├── src/ │ │ ├── main/ │ │ │ ├── res/web/ │ │ │ │ ├── index.html │ │ │ │ ├── styles.css │ │ │ │ ├── scripts.js │ ├── build.gradle.kts ├── scripts/ │ ├── setup_firebase.py │ ├── generate_data.py ├── .gitignore


## 🚀 How to Run

### Android App
1. Clone the repository:
   ```bash
   git clone https://github.com/Razworld00/RaznetRealTalkApp.git

Open the project in Android Studio.
Sync Gradle files and run the app on an emulator or a connected device:
bash
Copy code

Shift + F10



Here’s an updated README.md for the web interface version of the Raznet RealTalk App. The content integrates the previous README with the new web interface description.

The Python script below will also automatically update the README.md in the folder structure.

Updated README.md Content
markdown
Copy code
# Raznet RealTalk

Raznet RealTalk is a modern real-time chat application available as both a **web interface** and an **Android app**. It supports real-time chat functionality, user authentication, and seamless navigation between multiple screens.

## 📱 Features (Android Version)
- **User Authentication**: Secure login and signup using Firebase Authentication.
- **Real-Time Navigation**: Smooth navigation between screens (Login, Home, Chat, Profile) powered by Jetpack Compose.
- **Responsive UI**: Built with Material Design 3 components for a clean and intuitive user experience.
- **Modular Architecture**: Organized and maintainable code structure with separate files for each screen.
- **Firebase Integration**: Real-time database functionality integrated with Firebase services.

## 🌐 Features (Web Version)
- **Responsive Design**: Clean and modern UI built with HTML, CSS, and JavaScript to support mobile and desktop browsers.
- **Navigation System**: Includes login, home, chat, and profile screens, similar to the Android app.
- **Lightweight Framework**: Fully responsive using pure HTML, CSS, and JavaScript without requiring external libraries.
- **Expandable Architecture**: Designed to integrate with Firebase for future real-time chat functionality.

## 🛠️ Tech Stack
### Frontend (Android):
- **Jetpack Compose**: Modern declarative UI toolkit for Android.
- **Material Design 3**: Ensures responsive and attractive interfaces.

### Frontend (Web):
- **HTML5**: Semantic markup for a clean structure.
- **CSS3**: Responsive and modern styling with intuitive layouts.
- **JavaScript (ES6)**: Interactive navigation and dynamic behavior.

### Backend:
- **Firebase Authentication**: Handles user login and registration.
- **Firebase Realtime Database**: (Planned) For real-time chat and message synchronization.

## 📂 Project Structure

### Android
RaznetRealTalk/ ├── app/ │ ├── src/ │ │ ├── main/ │ │ │ ├── kotlin/com/example/raznetrealtalkapp/ │ │ │ │ ├── MainActivity.kt │ │ │ │ ├── LoginScreen.kt │ │ │ │ ├── GreetingScreen.kt │ │ │ │ ├── ChatScreen.kt │ │ │ │ ├── ProfileScreen.kt │ │ │ ├── AndroidManifest.xml │ ├── build.gradle.kts ├── build.gradle.kts ├── .gitignore

shell
Copy code

### Web Interface
RaznetRealTalk/ ├── app/ │ ├── src/ │ │ ├── main/ │ │ │ ├── res/web/ │ │ │ │ ├── index.html │ │ │ │ ├── styles.css │ │ │ │ ├── scripts.js │ ├── build.gradle.kts ├── scripts/ │ ├── setup_firebase.py │ ├── generate_data.py ├── .gitignore

bash
Copy code

## 🚀 How to Run

### Android App
1. Clone the repository:
   ```bash
   git clone https://github.com/Razworld00/RaznetRealTalkApp.git
Open the project in Android Studio.
Sync Gradle files and run the app on an emulator or a connected device:
bash
Copy code
Shift + F10
Web Version
Navigate to the app/src/main/res/web/ directory.
Open index.html in any modern web browser.
🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to check the issues page for outstanding tasks or create new ones.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.