package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View.GONE
import android.view.View.VISIBLE
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import com.example.project.R

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        var input = findViewById<EditText>(R.id.inputText)
        var word1 = findViewById<TextView>(R.id.Word1)
        var word2 = findViewById<TextView>(R.id.Word2)
        var word3 = findViewById<TextView>(R.id.Word3)
        var ans = "test"
        val next =findViewById<Button>(R.id.NextBtn)
        var btn = findViewById<Button>(R.id.submitBtn)
        word1.setText("thing 1")
        word2.setText("thing 2")
        word3.setText("thing 3")
        btn.setOnClickListener {
            if (input.text.contains(ans)) {
                word1.setText("correct")
                word2.setText("correct")
                word3.setText("correct")
                next.setVisibility(VISIBLE)
            }
        }
        next.setOnClickListener {
            word1.setText("thing 1")
            word2.setText("thing 2")
            word3.setText("thing 3")
            next.setVisibility(GONE)
            input.setText("Input")
        }
    }
}