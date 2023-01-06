package viewModel

import Backend.EstimHousedata
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class EstimhouseViewModel : ViewModel() {


    val estimationlivedata = MutableLiveData(0)
    private val estimationlivedatabackend = EstimHousedata()

    /* private var _update_value = MutableLiveData<Int>().apply { value = 0 }
    val update_value: LiveData<Int>
        get() = _update_value
    fun update(update_value: Int){
        _update_value.value = update_value
    }
*/
    fun estimation(surfacereelle: Double, type: Double, surfaceterrain: Double, nmdepiece: Double) {
        //  valuealeatsurface.value = estimHousedata.aleaval()
        // valuealeatcodepostal.value = estimHousedata2.aleaval()
        estimationlivedata.value = estimationlivedatabackend.estimation(surfacereelle, type, surfaceterrain, nmdepiece).toInt()
    }
}