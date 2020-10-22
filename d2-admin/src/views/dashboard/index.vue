<template>
  <d2-container>
    <template slot="header">仪表盘</template>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>集群资源展示</span>
        <ve-histogram :data="ClusterData" :extend="extend" ></ve-histogram>
      </div>
    </el-card>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>宿主机资源展示</span>
    <ve-line :data="HostData" :extend="extend2"></ve-line>
    <template slot="footer">footer</template>
      </div>
    </el-card>
  </d2-container>
</template>

<script>
import {getclusterhost,gethostresource,getdataresource} from '@api/vms'

export default {
  name: "dashboard",
  created () {
    this.GetClusterhostData()
    this.GetdedicatehostresourceData()

  },
  data () {
      return {
      extend: {
        series: {
          label: { show: true, position: 'top' }
        }
      },
      extend2: {'xAxis.0.axisLabel.rotate': 45},
      ClusterData: {
        columns: ['集群', '虚拟机数量', '宿主机数量' ],
        rows: []
      },
      HostData:{
        columns:['主机名','cpu总计/GHz','cpu已用/GHz','内存总计/G','内存已用/G'],
        rows:[]
      }
    }
  },
  methods:{
    GetClusterhostData(){
      getclusterhost().then(res=>{
        this.ClusterData.rows = res;
        console.log(this.ClusterData.rows)
      }).catch(function (error){
        console.log(error)
      })
    },
    GetdedicatehostresourceData(){
      gethostresource().then(res=>{
        this.HostData.rows = res;
        console.log(this.HostData.rows)
      }).catch(function (error){
        console.log(error)
      })
    },
  }
}

</script>

<style scoped>
</style>
