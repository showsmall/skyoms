<template>
  <d2-container type="card">
    <template slot="header">集群</template>
    <div class="handle-head">
    <div class="search" >
      <el-input v-model="table.getParams.search" placeholder="请输入集群名"  class="handle-input mr5" size="mini"  ></el-input>
      <el-button icon="el-icon-search"  size="mini" circle @click="getClusterData" style="margin-left: 10px"></el-button>
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
        height="250"
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
import { getcluster} from '@api/vms'
import Vue from 'vue'
import pluginExport from '@d2-projects/vue-table-export'
Vue.use(pluginExport)
export default {
  name: 'cluster',
  created () {
    this.getClusterData();
    for (let i = 0; i < this.table.columns.length; i++) {
      this.colSelect.push(this.table.columns[i].label);
      this.colOptions.push(this.table.columns[i].label);

    }
  },
  data () {
    return {
      colOptions: [],
      colSelect: [],
      table: {
        columns: [
          {
            label: 'ID',
            prop: 'id',
            sort:"custom",
          },
          {
            label: '集群名',
            prop: 'name',
            sort:false,
            width: 120,
          },
          {
            label: '数据中心',
            prop: 'datacenter',
            sort:false,
            width:150,
          },
          {
            label: 'CPU总计',
            prop: 'cputotal',
            sort:false,
            width: 130,
          },
          {
            label: 'CPU使用量',
            prop: 'cpuusage',
            sort:false,
            width: 130,
          },
          {
            label: '内存总计',
            prop: 'memtotal',
            sort:false,
            width: 130,
          },
          {
            label: '内存使用量',
            prop: 'memusage',
            sort:false,
            width: 130,
          },
          {
            label: '存储总计',
            prop: 'datatotal',
            sort:false,
            width: 130,
          },
          {
            label: '存储剩余量',
            prop: 'datafree',
            sort:false,
            width: 130,
          },
          {
            label: '宿主机数量',
            prop: 'numshosts',
            sort:false,
            width:110,
          },
          {
            label: '虚拟机数量',
            prop: 'vmscount',
            sort:"custom",
            width: 120,
          },

        ],
        data: [],
        size: 'mini',
        stripe: 'true',
        fit: 'true',
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
    exportExcel () {
      this.$export.excel({
        title : '集群列表',
        columns: this.table.columns,
        data: this.table.data,
      }).then(() => {
        this.$message('表格导出成功')
      })
    },
    //获取集群信息
    getClusterData () {
      getcluster(this.table.getParams).then(res => {
        console.log(this.table.getParams)
        this.table.data = res.results;
        this.table.total = res.count;
        console.log(this.table.data)
      }).catch(function (error) {
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
      this.getClusterData()
    },
    handleCurrentChange(page){
      this.table.getParams.page=page
      this.getClusterData()
    },
    handleSizeChange(size){
      this.table.getParams.page_size = size
      this.getClusterData()
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
        this.getClusterData()
        // this.table.data = this.table.data.sort((a, b) => b[fieldName] - a[fieldName]);
      }
      //按照升序排序
      else {
        this.table.getParams.ordering = fieldName
        this.getClusterData()
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
