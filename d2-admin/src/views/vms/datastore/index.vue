<template>
  <d2-container type="card">
    <template slot="header">存储</template>
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
        :label="item.label">
      </el-table-column>
    </el-table>
  </d2-container>
</template>

<script>
import Vue from 'vue'
import { getdatastore } from '@api/vms'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
export default {
name: 'datastore',
  created () {
    this.getDatastoreData();
  },
  data() {
    return {
      table: {
        columns:[
          {label:'ID',prop:'id'},
          {label:'存储名',prop:'name'},
          {label: '数据中心',prop: 'datacenter'},
          {label:'存储总计',prop:'capacity'},
          {label:'存储剩余量',prop:'freespace'},

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
        merges: ['A1','E1']
      }).then(()=>{
        this.$message('表格导出成功')
      })
    },
    //获取集群信息
    getDatastoreData() {
      getdatastore().then(res=>{
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
