<template>
  <d2-container type="card">
    <template slot="header">数据中心</template>
    <div class="download">
      <el-button type="primary" size="mini" round @click="exportExcel">
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
        :width="item.width">
      </el-table-column>
    </el-table>
  </d2-container>
</template>

<script>
import Vue from 'vue'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
import { getdatacenter } from '@api/vms'
export default {
name: 'datacenter',
  created () {
    this.getDatacenterData();
  },
  data() {
    return {
      table: {
        columns:[
          {label:'ID',prop:'id'},
          {label:'数据中心',prop:'name',width:'150'},
          {label:'CPU总计',prop:'cputotal',width:'130'},
          {label:'CPU使用量',prop:'cpuusage',width:'130'},
          {label:'内存总计',prop:'memtotal',width:'130'},
          {label:'内存使用量',prop:'memusage',width:'130'},
          {label:'存储总计',prop:'datatotal',width:'130'},
          {label:'存储剩余量',prop:'datafree',width:'130'},
          {label:'宿主机数量',prop:'numhosts',width:'110'},
          {label:'虚拟机数量',prop:'vmscount',width:'110'},
          {label:'CPU总核数',prop:'numcpuscores',width:'110'},

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
        title: '数据中心列表'
      }).then(()=>{
        this.$message('表格导出成功')
      })
    },
    //获取数据中心信息
    getDatacenterData() {
      getdatacenter().then(res=>{
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
.handle-head {
  padding-bottom: 5px;
}
.pagination {
  float: right;
  margin-top: 20px;
}
.search {
  float: left;
}
.handle-input {
  width: 300px;
  display: inline-block;
}
.download {
  margin-top: 5px;
  margin-bottom: 5px;
  margin-inside: 5px;
  float: right;
}

</style>

