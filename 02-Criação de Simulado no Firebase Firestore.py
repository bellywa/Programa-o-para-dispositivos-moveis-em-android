2. Criação de Simulado no Firebase Firestore
// Função para criar um novo simulado
fun createSimulado(simuladoTitle: String, questions: List<String>, answers: List<String>) {
    val simuladoData = hashMapOf(
        "title" to simuladoTitle,
        "questions" to questions,
        "answers" to answers,
        "createdAt" to FieldValue.serverTimestamp()
    )

    FirebaseFirestore.getInstance().collection("simulados")
        .add(simuladoData)
        .addOnSuccessListener { documentReference ->
            Log.d("Simulado", "Simulado criado com sucesso com ID: ${documentReference.id}")
        }
        .addOnFailureListener { e ->
            Log.e("Simulado", "Erro ao criar o simulado", e)
        }
}

