import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'WebVision',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  String _message = '';

  Future<void> login(String username, String password) async {
    final url = Uri.parse('https://webvision.onrender.com/login'); // 🌐 Modifica l’URL qui se necessario

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'username': username, 'password': password}),
      );

      if (response.statusCode == 200) {
        setState(() {
          _message = '✅ Login riuscito!';
        });

        // ✅ Navigazione alla pagina successiva (simulata)
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => SuccessPage()),
        );
      } else {
        setState(() {
          _message = '❌ Credenziali non valide';
        });
      }
    } catch (e) {
      setState(() {
        _message = '⚠️ Errore di connessione: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Login WebVision')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: usernameController,
              decoration: InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: passwordController,
              obscureText: true,
              decoration: InputDecoration(labelText: 'Password'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                login(usernameController.text, passwordController.text);
              },
              child: Text('Login'),
            ),
            SizedBox(height: 20),
            Text(_message, style: TextStyle(color: Colors.red)),
          ],
        ),
      ),
    );
  }
}

// ✅ Pagina successiva placeholder
class SuccessPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Benvenuto!')),
      body: Center(
        child: Text(
          '🎉 Accesso effettuato con successo!',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}
