4. Gerar Gráficos de Desempenho com MPAndroidChart

// Adicionar ao arquivo build.gradle
implementation 'com.github.PhilJay:MPAndroidChart:v3.1.0'

import com.github.mikephil.charting.charts.BarChart
import com.github.mikephil.charting.components.Description
import com.github.mikephil.charting.data.BarData
import com.github.mikephil.charting.data.BarDataSet
import com.github.mikephil.charting.data.BarEntry

fun setupPerformanceChart(barChart: BarChart, performanceData: Map<String, Float>) {
    val barEntries = ArrayList<BarEntry>()
    val labels = ArrayList<String>()

    var index = 0f
    for ((area, score) in performanceData) {
        barEntries.add(BarEntry(index, score))
        labels.add(area)
        index++
    }

    val barDataSet = BarDataSet(barEntries, "Desempenho por Área")
    val barData = BarData(barDataSet)
    barChart.data = barData

    // Customizando o gráfico
    val description = Description()
    description.text = "Desempenho em Simulados"
    barChart.description = description
    barChart.animateY