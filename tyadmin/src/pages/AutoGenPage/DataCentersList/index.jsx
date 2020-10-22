import {DownOutlined, PlusOutlined, EditOutlined,DeleteOutlined} from '@ant-design/icons';
import {Button, Divider, Dropdown, Input, Menu, message, Popconfirm, Select, Switch, Tag, Space} from 'antd';
import React, {useEffect,useRef, useState} from 'react';
import {PageHeaderWrapper} from '@ant-design/pro-layout';
import ProTable from 'mtianyan-pro-table';
import CreateForm from './components/CreateForm';
import {addDataCenters, queryDataCenters, removeDataCenters, updateDataCenters} from './service';
import UpdateForm from './components/UpdateForm';
import UploadAvatar from '@/components/UploadAvatar';

import moment from 'moment';
const {Option} = Select;
import {BooleanDisplay, dealDateTimeDisplay, dealTime, deepCopy, getObjectClass, getTableColumns, richForm, richTrans, richCol,fileUpload} from '@/utils/utils';
import 'braft-editor/dist/index.css'

const TableList = () => {
  const [createModalVisible, handleModalVisible] = useState(false);
  const [updateModalVisible, handleUpdateModalVisible] = useState(false);
  const [updateFormValues, setUpdateFormValues] = useState({});
  const actionRef = useRef();
  const addFormRef = useRef();
  const updateFormRef = useRef();

  const handleAdd = async fields => {
  const hide = message.loading('正在添加');

  try {
    await addDataCenters({...fields});
    hide();
    message.success('添加成功');
    return true;
  } catch (error) {
      if ('fields_errors' in error.data) {
        for (let key in error.data.fields_errors) {
          var value = error.data.fields_errors[key];
          addFormRef.current.setFields([
            {
              name: key,
              errors: value,
            },
          ]);
        }
      } else {
        message.error('非字段类型错误');
      }
    hide();
    message.error('添加失败');
    return false;
  }
};

  const handleUpdate = async (value, current_id) => {
  const hide = message.loading('正在修改');

  try {
    await updateDataCenters(value, current_id);
    hide();
    message.success('修改成功');
    return true;
  } catch (error) {
            if ('fields_errors' in error.data) {
        for (let key in error.data.fields_errors) {
          var value = error.data.fields_errors[key];
          updateFormRef.current.setFields([
            {
              name: key,
              errors: value,
            },
          ]);
        }
      } else {
        message.error('非字段类型错误');
      }
    hide();
    message.error('修改失败请重试！');
    return false;
  }
};

  const handleRemove = async selectedRows => {
  const hide = message.loading('正在删除');
  if (!selectedRows) return true;

  try {
    const ids = selectedRows.map(row => row.id).join(',');
    await removeDataCenters(ids);
    hide();
    message.success('删除成功');
    return true;
  } catch (error) {
    hide();
    message.error('删除失败，请重试');
    return false;
  }
};
  const dateFieldList = ["ctime","utime"]
  const base_columns = [{
                                  title: 'ID',
                                  dataIndex: 'id',
                                  hideInForm: true,
                                  hideInSearch: true,
                                  rules: [
                                    {
                                      required: true,
                                      message: 'ID为必填项',
                                    },
                                  ],
                                },{
                      title: '数据中心名',
                      dataIndex: 'name',
                      rules: [
                        {
                          required: true,
                          message: '数据中心名为必填项',
                        },
                      ],
                    },{
                      title: 'CPU总计',
                      dataIndex: 'cputotal',
                      rules: [
                        {
                          required: true,
                          message: 'CPU总计为必填项',
                        },
                      ],
                    },{
                      title: 'CPU使用量',
                      dataIndex: 'cpuusage',
                      rules: [
                        {
                          required: true,
                          message: 'CPU使用量为必填项',
                        },
                      ],
                    },{
                      title: '内存总计',
                      dataIndex: 'memtotal',
                      rules: [
                        {
                          required: true,
                          message: '内存总计为必填项',
                        },
                      ],
                    },{
                      title: '内存使用量',
                      dataIndex: 'memusage',
                      rules: [
                        {
                          required: true,
                          message: '内存使用量为必填项',
                        },
                      ],
                    },{
                      title: '存储总计',
                      dataIndex: 'datatotal',
                      rules: [
                        {
                          required: true,
                          message: '存储总计为必填项',
                        },
                      ],
                    },{
                      title: '存储剩余量',
                      dataIndex: 'datafree',
                      rules: [
                        {
                          required: true,
                          message: '存储剩余量为必填项',
                        },
                      ],
                    },{
                                      title: '宿主机数量',
                                      dataIndex: 'numhosts',
                                                valueType: 'digit',
                                      rules: [
                                        {
                                          required: true,
                                          message: '宿主机数量为必填项',
                                        },
                                      ],
                                    },{
                                      title: 'CPU总核数',
                                      dataIndex: 'numcpuscores',
                                                valueType: 'digit',
                                      rules: [
                                        {
                                          required: true,
                                          message: 'CPU总核数为必填项',
                                        },
                                      ],
                                    },{
                                      title: '虚拟机数量',
                                      dataIndex: 'vmscount',
                                                valueType: 'digit',
                                      rules: [
                                        {
                                          required: true,
                                          message: '虚拟机数量为必填项',
                                        },
                                      ],
                                    },{
                                  title: '描述',
                                  dataIndex: 'desc',
                                valueType: 'textarea',
                                 ellipsis: true,
                                  rules: [
                                    {
                                      required: true,
                                      message: '描述为必填项',
                                    },
                                  ],
                                },{
              title: '创建时间',
              dataIndex: 'ctime',
              valueType: 'dateTime',
              hideInForm: true,
              rules: [
                {
                  required: true,
                  message: '创建时间为必填项',
                },
              ],
                                       render: (text, record) => {
          return dealDateTimeDisplay(text);
        },
            },{
              title: '更新时间',
              dataIndex: 'utime',
              valueType: 'dateTime',
              hideInForm: true,
              rules: [
                {
                  required: true,
                  message: '更新时间为必填项',
                },
              ],
                                       render: (text, record) => {
          return dealDateTimeDisplay(text);
        },
            },    {
                              title: '操作',
                              dataIndex: 'option',
                              valueType: 'option',
                                    fixed: 'right',
          width: 100,
                              render: (text, record) => (
                                <>
    
                                  <EditOutlined title="编辑" className="icon" onClick={async () => {
                                    record.ctime = moment(record.ctime);record.utime = moment(record.utime);
                                    handleUpdateModalVisible(true);
                                    setUpdateFormValues(record);
                                  }} />
                                  <Divider type="vertical" />
                                  <Popconfirm
                                    title="您确定要删除数据中心吗？"
                                    placement="topRight"
                                    onConfirm={() => {
                                      handleRemove([record])
                                      actionRef.current.reloadAndRest();
                                    }}
                                    okText="确定"
                                    cancelText="取消"
                                  >
                                    <DeleteOutlined title="删除" className="icon" />
                                  </Popconfirm>
                                </>
                              ),
                            },];

  let cp = deepCopy(base_columns);
  const table_columns = getTableColumns(cp);

  const update_columns = [...base_columns];

  const create_columns = [...base_columns];

  const [columnsStateMap, setColumnsStateMap] = useState({});

  const [paramState, setParamState] = useState({});

  


    
  return (
    <PageHeaderWrapper>
      <ProTable
           beforeSearchSubmit={(params => {
                         dealTime(params, dateFieldList);
          return params;
        })}
        params={paramState}
        scroll={{x: '100%'}}
        columnsStateMap={columnsStateMap}
        onColumnsStateChange={(map) => setColumnsStateMap(map)}
        headerTitle="数据中心表格"
        actionRef={actionRef}
        rowKey="id"
        toolBarRender={(action, {selectedRows}) => [
          <Button type="primary" onClick={() => handleModalVisible(true)}>
            <PlusOutlined /> 新建
          </Button>,
          <Input.Search style={{marginRight: 20}} placeholder="搜索数据中心 " onSearch={value => {
            setParamState({
              search: value,
            });
            actionRef.current.reload();
          }} />,
          selectedRows && selectedRows.length > 0 && (
            <Dropdown
              overlay={
                <Menu
                  onClick={async e => {
                    if (e.key === 'remove') {
                      await handleRemove(selectedRows);
                      actionRef.current.reloadAndRest();
                    }
                  }}
                  selectedKeys={[]}
                >
                  <Menu.Item key="remove">批量删除</Menu.Item>
                </Menu>
              }
            >
              <Button>
                批量操作 <DownOutlined />
              </Button>
            </Dropdown>
          ),
        ]}
        tableAlertRender={({selectedRowKeys, selectedRows}) => (
          selectedRowKeys.length > 0 ? <div>
            已选择{' '}
            <a
              style={{
                fontWeight: 600,
              }}
            >
              {selectedRowKeys.length}
            </a>{' '}
            项&nbsp;&nbsp;
          </div> : false

        )}
        request={(params, sorter, filter) => queryDataCenters({...params, sorter, filter})}
        columns={table_columns}
        rowSelection={{}}
      />
      <CreateForm onCancel={() => handleModalVisible(false)} modalVisible={createModalVisible}>
        <ProTable
                     formRef={addFormRef}
          onSubmit={async value => {
                          richTrans(value);
            const success = await handleAdd(value);

            if (success) {
              handleModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          type="form"
                    search={{
                                span: {
                                  lg: 12,
                                  md: 12,
                                  xxl: 12,
                                  xl: 12,
                                  sm: 12,
                                  xs: 24,
                                },
                              }}
          form={
            {
              labelCol: {span: 6},
              labelAlign: 'left',
            }}
          columns={create_columns}
          rowSelection={{}}
        />
      </CreateForm>
      <UpdateForm onCancel={() => handleUpdateModalVisible(false)} modalVisible={updateModalVisible}>
        <ProTable
          formRef={updateFormRef}
          onSubmit={async value => {
                          richTrans(value);
            const success = await handleUpdate(value, updateFormValues.id);

            if (success) {
              handleUpdateModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
                    search={{
                                span: {
                                  lg: 12,
                                  md: 12,
                                  xxl: 12,
                                  xl: 12,
                                  sm: 12,
                                  xs: 24,
                                },
                              }}
          type="form"
          form={{
            initialValues: updateFormValues, labelCol: {span: 6},
            labelAlign: 'left',
          }}
          columns={update_columns}
          rowSelection={{}}
        />
      </UpdateForm>
    </PageHeaderWrapper>
  );
};

export default TableList;
