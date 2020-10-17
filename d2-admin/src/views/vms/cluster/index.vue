<template>
  <d2-container type="card">
    <template slot="header">集群</template>
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
import { getcluster} from '@api/vms'
import Vue from 'vue'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
export default {
  name: 'cluster',
  created () {
    this.getClusterData();
  },
  data() {
    return {
      table: {
        columns:[
          {label:'ID',prop:'id'},
          {label:'集群名',prop:'name'},
          {label: '数据中心',prop: 'datacenter'},
          {label:'CPU总计',prop:'cputotal'},
          {label:'CPU使用量',prop:'cpuusage'},
          {label:'内存总计',prop:'memtotal'},
          {label:'内存使用量',prop:'memusage'},
          {label:'存储总计',prop:'datatotal'},
          {label:'存储剩余量',prop:'datafree'},
          {label:'宿主机数量',prop:'numshosts'},
          {label:'虚拟机数量',prop:'vmscount'},

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
      merges: ['A1','K1']
    }).then(()=>{
      this.$message('表格导出成功')
    })
  },
  //获取集群信息
  getClusterData() {
      getcluster().then(res=>{
        this.table.data = res;
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
