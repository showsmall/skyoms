<template>
  <d2-container type="card">
    <template slot="header">存储</template>
    <div class="handle-head">
      <div class="search" >
        <el-input v-model="table.getParams.search" placeholder="请输入存储名"  class="handle-input mr5" size="mini"  ></el-input>
        <el-button icon="el-icon-search"  size="mini" circle @click="getDatastoreData" style="margin-left: 10px"></el-button>
        <el-button size="mini"  icon="el-icon-refresh" circle @click="refreshClick"></el-button>
      </div>
      <div class="download">
        <el-button type="primary" size="mini" round @click="exportExcel">
          <d2-icon name="download"/>导出Excel
        </el-button>
      </div>
    </div>
    <el-table
      :data="table.data"
      style="width: 100%"
      @sort-change="changeTableSort"
      v-if="table.data.length>0"
    >
      <el-table-column
        v-for="(item,index) in table.columns"
        :sortable=item.sort
        :key="index"
        :prop="item.prop"
        :label="item.label"
        :width="item.width"
        show-overflow-tooltip>
      </el-table-column>
    </el-table>
    <div class="d2-crud-footer">
      <div class="d2-crud-pagination">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="table.getParams.page"
          :page-sizes="[10, 20, 50,100,500]"
          :page-size="table.getParams.page_size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="table.total">
        </el-pagination>
      </div>
    </div>
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
          //{label:'ID',prop:'id',sort:'custom'},
          {label:'存储名',prop:'name',sort:false},
          {label: '数据中心',prop: 'datacenter',sort: false},
          {label:'存储总计',prop:'capacity',sort: false},
          {label:'存储剩余量',prop:'freespace',sort: 'custom'},

        ],
        data : [],
        size: 'mini',
        stripe: 'true',
        fit:'true',
        getParams:{
          page:1,
          page_size:10,
          search:'',
          ordering:''
        },
        total:0,

      }
    }
  },
  methods: {
    //导出excel
    exportExcel() {
      this.$export.excel({
        columns: this.table.columns,
        data: this.table.data,
        title: '存储列表'
      }).then(()=>{
        this.$message('表格导出成功')
      })
    },
    //获取集群信息
    getDatastoreData() {
      getdatastore(this.table.getParams).then(res=>{
        this.table.data = res.results;
        this.table.total = res.count;
      }).catch(function (error){
        console.log(error)
      })
    },
    refreshClick(){
      this.table.getParams = {
        page:1,
        page_size:10,
        search:'',
        ordering:''
      };
      this.getDatastoreData();
    },
    handleCurrentChange(page){
      this.table.getParams.page=page
      this.getDatastoreData();
    },
    handleSizeChange(size){
      this.table.getParams.page_size = size
      this.getDatastoreData();
    },
    //对指定字段排序
    changeTableSort (column) {
      console.log(column);
      //  获取字段名和排序类型
      var fieldName = column.prop;
      var sortingType = column.order;
      //按照降序排序
      if (sortingType === "descending") {
        this.table.getParams.ordering = '-' + fieldName
        this.getDatastoreData();
        // this.table.data = this.table.data.sort((a, b) => b[fieldName] - a[fieldName]);
      }
      //按照升序排序
      else {
        this.table.getParams.ordering = fieldName
        this.getDatastoreData();
        //this.table.data = this.table.data.sort((a, b) => a[fieldName] - b[fieldName]);

      }
    },
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
