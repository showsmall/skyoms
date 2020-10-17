import store from '@/store/index'
import {getinnatehosts} from '@api/vms'

export default {
  namespace :true,
  state: {
    cluster:[],
    datacenter:[],
    datastore:[],
    virtualhost:[],
    innatehost:[]
  },
  actions:{

  }


}
