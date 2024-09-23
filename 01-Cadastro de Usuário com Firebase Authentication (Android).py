1. Cadastro de Usuário com Firebase Authentication (Android)

// Dependências no build.gradle
implementation 'com.google.firebase:firebase-auth:21.0.1'
implementation 'com.google.firebase:firebase-firestore:24.0.1'

// Função para registrar novo aluno
fun registerUser(email: String, password: String) {
    FirebaseAuth.getInstance().createUserWithEmailAndPassword(email, password)
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                // Registro bem-sucedido
                val user = FirebaseAuth.getInstance().currentUser
                user?.let {
                    // Salvando dados adicionais do aluno no Firestore
                    val userData = hashMapOf(
                        "email" to email,
                        "userId" to it.uid
                    )
                    FirebaseFirestore.getInstance().collection("users").document(it.uid)
                        .set(userData)
                        .addOnSuccessListener {
                            Log.d("Register", "Usuário registrado com sucesso no Firestore")
                        }
                        .addOnFailureListener { e ->
                            Log.e("Register", "Erro ao registrar no Firestore", e)
                        }
                }
            } else {
                Log.e("Register", "Falha ao registrar o usuário", task.exception)
            }
        }
}