package viewModel

import Backend.EstimHousedata
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import com.example.estimhouse.MainActivity

class EstimhouseViewModel : ViewModel(){

    val valuealeatsurface = MutableLiveData(0)
    val valuealeatcodepostal = MutableLiveData(0)
    val estimationlivedata = MutableLiveData(0)
    private val estimHousedata = EstimHousedata()
    private val estimHousedata2 = EstimHousedata()
    private val estimationlivedatabackend = EstimHousedata()

    /* private var _update_value = MutableLiveData<Int>().apply { value = 0 }
     val update_value: LiveData<Int>
         get() = _update_value
     fun update(update_value: Int){
         _update_value.value = update_value
     }
 */
    fun aleaval(){
        //  valuealeatsurface.value =     estimHousedata.aleaval()
        // valuealeatcodepostal.value = estimHousedata2.aleaval()
        estimationlivedata.value = estimationlivedatabackend.aleaval()
    }

}
/*
class EstimhouseViewModel(state: SavedStateHandle): ViewModel(){

    private val _valuealeatcodepostal = state.getLiveData("",0)
    val valuealeatcodepostal : LiveData<Int> = _valuealeatcodepostal

    private val _valuealeatsurface = state.getLiveData("",0)
    val valuealeatsurface : LiveData<Int> = _valuealeatsurface

    private val estimationBackend = EstimHousedata()
    private val _estimationlivedata = state.getLiveData("",0)
    val estimationlivedata : LiveData<Int> = _estimationlivedata

    fun aleaval(){
        _estimationlivedata.value=estimationBackend.aleaval()
    }

}*/
