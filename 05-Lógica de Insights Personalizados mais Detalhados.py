5. Lógica de Insights Personalizados mais Detalhados


fun generateDetailedInsights(questions: List<String>, correctAnswers: List<Boolean>, topics: List<String>) {
    val insights = mutableMapOf<String, MutableList<String>>()

    for ((index, isCorrect) in correctAnswers.withIndex()) {
        val topic = topics[index]
        val question = questions[index]
        
        if (!isCorrect) {
            // Adiciona feedback específico ao tema
            if (!insights.containsKey(topic)) {
                insights[topic] = mutableListOf()
            }
            insights[topic]?.add("Você errou a questão: $question. Revisar o tópico: $topic.")
        }
    }

    for ((topic, feedbackList) in insights) {
        Log.d("Insights", "Área: $topic")
        for (feedback in feedbackList) {
            Log.d("Insights", feedback)
        }
    }
}