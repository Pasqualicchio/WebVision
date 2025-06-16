plugins {
    id("com.android.application")
    id("kotlin-android")
    // Flutter plugin deve venire dopo
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.example.web_vision"
    compileSdk = flutter.compileSdkVersion

    // ✅ Aggiunto per risolvere il problema NDK
    ndkVersion = "27.0.12077973"

    defaultConfig {
        applicationId = "com.example.web_vision"
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    kotlinOptions {
        jvmTarget = "11"
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

flutter {
    source = "../.."
}
