package com.example.estimhouse

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.activity.viewModels

import com.example.estimhouse.databinding.ActivityMainBinding
import viewModel.EstimhouseViewModel

class MainActivity : AppCompatActivity() {
    private val  estimhouseViewModel : EstimhouseViewModel by viewModels()
    @SuppressLint("StringFormatInvalid", "StringFormatMatches", "SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.estimationText.visibility = View.GONE

        binding.estimationVal.visibility = View.GONE

        binding.validateButton.setOnClickListener{
        
        // Après l'appui sur le bouton, les valeurs des champs sont stokées dans des variables '
        
            val savesurfacevalue : Double = binding.surface.text.toString().toDouble()

            val nmbofroom : Double = binding.nombredepiece.text.toString().toDouble()

            val savesurfareel : Double = binding.surfacereel.text.toString().toDouble()

            val savetypevalue :Double = binding.type.text.toString().toDouble()
            
        // L'appui sur le bouton déclanche l'appel à la fonction estimation du viewModel qui communique avec le backend,
        // et renvoie l'estimation' 
            
            estimhouseViewModel.estimation(savesurfacevalue,savetypevalue,savesurfareel,nmbofroom)

            binding.Titre.visibility= View.GONE
            binding.type.visibility = View.GONE
            binding.surface.visibility = View.GONE
            binding.validateButton.visibility = View.GONE
            binding.surface.visibility = View.GONE
            binding.surfacereel.visibility = View.GONE
            binding.nombredepiece.visibility = View.GONE

            binding.estimationText.visibility = View.VISIBLE
            binding.estimationVal.visibility = View.VISIBLE
           /* binding.nombredepiece.text = binding.nombredepiece.text
              binding.surfaceText.text = binding.surface.text*/



        }
	
	// Stockage de valeur dans la liveData
        estimhouseViewModel.estimationlivedata.observe(this){ value->
            binding.estimationVal.text = getString(R.string.estimationlivedata,value)
        }

        /* estimhouseViewModel.valuealeatsurface.observe(this){ value->
                binding.surfaceText.text = getString(R.string.surface,value)
            }*/


    }

}
