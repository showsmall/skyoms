<template>
  <d2-container>
    <template slot="header">仪表盘</template>
    <ve-histogram :data="chartData" :extend="extend" ></ve-histogram>
    <template slot="footer">footer</template>
  </d2-container>
</template>

<script>
import {getclusterhost} from '@api/vms'

export default {
  name: "dashboard",
  created () {
    this.GetClusterhostData()
  },
  data () {
    return {
      extend: {
        series: {
          label: { show: true, position: 'top' }
        }
      },
      chartData: {
        columns: ['集群', '虚拟机数量', '宿主机数量' ],
        rows: []
      }
    }
  },
  methods:{
    GetClusterhostData(){
      getclusterhost().then(res=>{
        this.chartData.rows = res;
        console.log(this.chartData.rows)
      }).catch(function (error){
        console.log(error)
      })
    }
  }
}

</script>

<style scoped>

</style>
