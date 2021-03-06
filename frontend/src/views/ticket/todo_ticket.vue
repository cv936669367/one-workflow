<template>
  <div class="app-container">
    <el-table
      :data="list"
      v-loading="listLoading"
      style="width: 100%"
      highlight-current-row
      @sort-change="handleSortChange"
    >
      <el-table-column label="名称" prop="name"></el-table-column>
      <el-table-column label="工单流水号" prop="sn" width="240">
        <template slot-scope="{ row }">
          <router-link :to="'/s_ticket/' + row.id">
            <el-link type="success">{{ row.sn }}</el-link>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="申请人" prop="create_user">
        <template slot-scope="{ row }">
          <span>{{ row.create_user.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="当前环节" prop="state">
        <template slot-scope="{ row }">
          <span>{{ row.state.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="当前状态" prop="transition">
        <template slot-scope="{ row }">
          <span>{{ row.transition.attribute_type | AttributeTypeFilter }}</span>
        </template>
      </el-table-column>
      <el-table-column label="申请人" prop="create_user">
        <template slot-scope="{ row }">
          <span>{{ row.create_user.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" prop="create_time"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ticket, auth } from "@/api/all";
import Pagination from "@/components/Pagination";
import {
  checkAuthAdd,
  checkAuthDel,
  checkAuthView,
  checkAuthUpdate,
} from "@/utils/permission";
import { mapGetters } from "vuex";

export default {
  name: "todo_ticket",

  components: { Pagination },
  data() {
    return {
      operationList: [],
      permissionList: {
        add: false,
        del: false,
        view: false,
        update: false,
      },
      list: [],
      total: 0,
      listLoading: true,
      listQuery: {
        // offset: 1,
        // limit: 20,
        search: undefined,
        ordering: undefined,
        participant: this.username,
        transition__attribute_type__lt: 4,
      },
    };
  },
  computed: {
    ...mapGetters(["username"]),
  },
  created() {
    this.getMenuButton();
    this.getList();
  },
  methods: {
    checkPermission() {
      this.permissionList.add = checkAuthAdd(this.operationList);
      this.permissionList.del = checkAuthDel(this.operationList);
      this.permissionList.view = checkAuthView(this.operationList);
      this.permissionList.update = checkAuthUpdate(this.operationList);
    },
    getMenuButton() {
      auth
        .requestMenuButton("todo_ticket")
        .then((response) => {
          this.operationList = response.results;
        })
        .then(() => {
          this.checkPermission();
        });
    },
    getList() {
      this.listLoading = true;
      this.listQuery.participant = this.username;
      ticket.requestGet(this.listQuery).then((response) => {
        this.list = response.results;
        this.listLoading = false;
      });
    },
    handleFilter() {
      this.getList();
    },
    handleSortChange(val) {
      if (val.order === "ascending") {
        this.listQuery.ordering = val.prop;
      } else if (val.order === "descending") {
        this.listQuery.ordering = "-" + val.prop;
      } else {
        this.listQuery.ordering = "";
      }
      this.getList();
    },
    handleDelete(row) {
      this.$confirm("是否确定删除?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          ticket.requestDelete(row.id).then(() => {
            this.$message({
              message: "删除成功",
              type: "success",
            });
            this.getList();
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>
