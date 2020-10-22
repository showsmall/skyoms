<template>
  <d2-container type="card">
    <template slot="header">宿主机</template>
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
import { getdedicatedhost } from '@api/vms'
import Vue from 'vue'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
export default {
name: 'dedicatedhost',
  created () {
    this.getDedicatedhostData();
  },
  data() {
    return {
      table: {
        columns:[
          {label:'ID',prop:'id'},
          {label:'宿主机',prop:'name'},
          {label: '数据中心',prop: 'datacenter'},
          {label: '集群',prop: 'cluster'},
          {label:'连接状态',prop:'conState'},
          {label:'电源状态',prop:'powerState'},
          {label:'CPU类型',prop:'cpumodel'},
          {label:'CPU数量',prop:'cpunums'},
          {label:'CPU核数',prop:'cpucores'},
          {label:'CPU总量',prop:'cputotal'},
          {label:'CPU用量',prop:'cpuusage'},
          {label:'内存总量',prop:'memtotal'},
          {label:'内存用量',prop:'memusage'},
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
        merges: ['A1','M1']
      }).then(()=>{
        this.$message('表格导出成功')
      })
    },
    //获取宿主机信息
    getDedicatedhostData() {
      getdedicatedhost().then(res=>{
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
