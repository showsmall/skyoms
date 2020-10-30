<template>
  <d2-container type="card">
    <template slot="header">网络</template>
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
        width="100">
      </el-table-column>
    </el-table>
  </d2-container>
</template>

<script>
import { getnetworkadapter } from '@api/vms'
import Vue from 'vue'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
export default {
name: 'networkadapter',
  created () {
    this.getNetworkadapterData();
  },
  data() {
    return {
      table: {
        columns:[
          {label:'ID',prop:'id'},
          {label:'网络名',prop:'name'},
          {label: '数据中心',prop: 'datacenter'},
          {label:'Vlan',prop:'vlanid'},
          {label:'类型',prop:'type'},

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
        title: '网络列表'
      }).then(()=>{
        this.$message('表格导出成功')
      })
    },
    //获取网络信息
    getNetworkadapterData() {
      getnetworkadapter().then(res=>{
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
