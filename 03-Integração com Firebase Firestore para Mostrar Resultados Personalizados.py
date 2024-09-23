3. Integração com Firebase Firestore para Mostrar Resultados Personalizados


// Função para buscar os resultados do aluno e gerar insights
fun fetchSimuladoResults(userId: String) {
    FirebaseFirestore.getInstance().collection("simulados")
        .whereEqualTo("userId", userId)
        .get()
        .addOnSuccessListener { documents ->
            for (document in documents) {
                val questions = document.get("questions") as List<String>
                val answers = document.get("answers") as List<String>

                // Lógica para comparar respostas e gerar insights
                generateInsights(questions, answers)
            }
        }
        .addOnFailureListener { e ->
            Log.e("Results", "Erro ao buscar resultados do simulado", e)
        }
}

fun generateInsights(questions: List<String>, answers: List<String>) {
    // Exemplo simples de lógica para gerar insights personalizados
    for ((index, question) in questions.withIndex()) {
        val answer = answers[index]
        if (answer == "correta") {
            Log.d("Insights", "Questão $question foi respondida corretamente")
        } else {
            Log.d("Insights", "Questão $question foi respondida incorretamente. Revisar o tema!")
        }
    }
}
