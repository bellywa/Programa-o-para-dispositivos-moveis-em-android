6. Salvando Dados de Progresso e Notificações no Firebase Firestore


fun saveUserProgress(userId: String, progressData: Map<String, Float>) {
    val progressRef = FirebaseFirestore.getInstance().collection("userProgress").document(userId)

    progressRef.set(progressData)
        .addOnSuccessListener {
            Log.d("Progress", "Progresso do usuário salvo com sucesso")
        }
        .addOnFailureListener { e ->
            Log.e("Progress", "Erro ao salvar progresso do usuário", e)
        }
}

// Exemplo de envio de notificação baseada no progresso
fun sendReviewNotification(userId: String, topic: String) {
    FirebaseFirestore.getInstance().collection("users").document(userId)
        .get()
        .addOnSuccessListener { document ->
            val userEmail = document.getString("email")
            userEmail?.let {
                // Lógica para enviar uma notificação personalizada
                Log.d("Notification", "Enviar e-mail para $it: Revisar o tópico $topic.")
                // Aqui, você integraria uma API de envio de e-mails ou notificações
            }
        }
}

// Exemplo de uso
val progressData = mapOf(
    "Genética" to 70f,
    "Ecologia" to 50f,
    "Biologia Celular" to 90f,
    "Fisiologia" to 60f
)
saveUserProgress("user123", progressData)
sendReviewNotification("user123", "Ecologia")