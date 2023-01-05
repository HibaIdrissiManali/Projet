package com.example.estimhouse

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.activity.viewModels

import com.example.estimhouse.databinding.ActivityMainBinding
import viewModel.EstimhouseViewModel

class MainActivity : AppCompatActivity() {
    val estimhouseViewModel : EstimhouseViewModel by viewModels()
    @SuppressLint("StringFormatInvalid", "StringFormatMatches", "SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.estimationText.visibility = View.GONE
        //   binding.valuealeatcodepostalText.visibility = View.GONE
        binding.estimationVal.visibility = View.GONE

        binding.validateButton.setOnClickListener{
            estimhouseViewModel.aleaval()

            binding.Titre.visibility= View.GONE
            binding.surface.visibility = View.GONE
            binding.validateButton.visibility = View.GONE
            binding.surface.visibility = View.GONE
            binding.surfacereel.visibility = View.GONE
            binding.nombredepiece.visibility = View.GONE

            binding.estimationText.visibility = View.VISIBLE
            binding.estimationVal.visibility = View.VISIBLE
            binding.nombredepiece.text = binding.nombredepiece.text
            binding.surfaceText.text = binding.surface.text



        }

        estimhouseViewModel.estimationlivedata.observe(this){ value->
            binding.estimationVal.text = getString(R.string.estimationlivedata,value)
        }

        /* estimhouseViewModel.valuealeatsurface.observe(this){ value->
                binding.surfaceText.text = getString(R.string.surface,value)
            }*/

        var savesurfacevalue : String
        savesurfacevalue = binding.surface.text.toString()

        var nmbofroom : String
        nmbofroom = binding.nombredepiece.text.toString()

        var savesurfareel : String
        savesurfareel = binding.surfacereel.text.toString()

        var savtypevalue :String
        savtypevalue = binding.type.text.toString()


        /*
        setContentView(binding.root)
        binding.validateButton.setOnClickListener {
            binding.surfaceText.text= binding.surface.text
            binding.adresseNomVoie.visibility = View.GONE
            binding.nomCommune.visibility = View.GONE
            binding.codePostal.visibility = View.GONE
            binding.surface.visibility = View.GONE
        }
        */

    }

}