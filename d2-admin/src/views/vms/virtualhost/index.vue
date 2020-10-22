<template>
  <d2-container type="card">
    <template slot="header">虚拟机</template>
    <div class="d2-mb">
      <el-button type="primary" @click="exportExcel">
        <d2-icon name="download"/>导出Excel
      </el-button>
    </div>
    <el-table
      :data="table.data"
      style="width: 100%"
      :default-sort = "{prop: 'id', order: 'descending'}"
      v-if="table.data.length>0"
    >
      <el-table-column
        v-for="(item,index) in table.columns"
        :key="index"
        :prop="item.prop"
        :label="item.label"
        width="100">
      </el-table-column>
    </el-table>
  </d2-container>
</template>

<script>
import { getvirtualhost } from '@api/vms'
import Vue from 'vue'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
export default {
name: 'virtualhost',
  created () {
    this.getVirtualhostData();
  },
  data() {
    return {
      table: {
        columns:[
          {label:'ID',prop:'id'},
          {label:'虚拟机名称',prop:'name'},
          {label:'数据中心',prop:'datacenter'},
          {label:'宿主机',prop:'ip'},
          {label:'电源状态',prop:'powerState'},
          {label:'CPU核数',prop:'cpunums'},
          {label:'内存',prop:'memtotal'},
          {label:'网络',prop:'network'},
          {label:'系统',prop:'os'},
          {label:'CPU用量',prop:'cpuusage'},
          {label:'内存用量',prop:'memusage'},
          {label:'存储用量',prop:'store_usage'},
        ],
        data : [],
        size: 'mini',
        stripe: 'true',
        fit:'true'

      }
    }
  },
  methods: {
    //导出excel
    exportExcel() {
      this.$export.excel({
        columns: this.table.columns,
        data: this.table.data,
        //header: '导出excel',
        merges: ['A1','L1']
      }).then(()=>{
        this.$message('表格导出成功')
      })
    },
    //获取所以虚拟机信息
    getVirtualhostData() {
      getvirtualhost ().then(res=>{
        this.table.data = res.results;
        console.log(this.table.data)
      }).catch(function (error){
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
