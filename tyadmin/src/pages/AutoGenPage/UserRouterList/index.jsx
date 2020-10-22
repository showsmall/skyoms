import {DownOutlined, PlusOutlined, EditOutlined,DeleteOutlined} from '@ant-design/icons';
import {Button, Divider, Dropdown, Input, Menu, message, Popconfirm, Select, Switch, Tag, Space} from 'antd';
import React, {useEffect,useRef, useState} from 'react';
import {PageHeaderWrapper} from '@ant-design/pro-layout';
import ProTable from 'mtianyan-pro-table';
import CreateForm from './components/CreateForm';
import {addUserRouter, queryUserRouter, removeUserRouter, updateUserRouter} from './service';
import UpdateForm from './components/UpdateForm';
import UploadAvatar from '@/components/UploadAvatar';
import {queryPermission} from '@/pages/AutoGenPage/PermissionList/service';
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
    await addUserRouter({...fields});
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
    await updateUserRouter(value, current_id);
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
    await removeUserRouter(ids);
    hide();
    message.success('删除成功');
    return true;
  } catch (error) {
    hide();
    message.error('删除失败，请重试');
    return false;
  }
};
  const dateFieldList = []
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
                      title: '路由路径',
                      dataIndex: 'path',
                      rules: [
                        {
                          required: true,
                          message: '路由路径为必填项',
                        },
                      ],
                    },{
                      title: '路由英文名称',
                      dataIndex: 'name',
                      rules: [
                        {
                          required: true,
                          message: '路由英文名称为必填项',
                        },
                      ],
                    },{
                      title: '路由中文标题',
                      dataIndex: 'title',
                      rules: [
                        {
                          required: true,
                          message: '路由中文标题为必填项',
                        },
                      ],
                    },{
                                  title: '是否需要验证',
                                  dataIndex: 'auth',
                                  rules: [
                                    {
                                      required: true,
                                      message: '是否需要验证为必填项',
                                    },
                                  ],
                                      render: (text, record) => {
          return BooleanDisplay(text);
        },
                                      renderFormItem: (_, {type, defaultRender, ...rest}, form) => {
          const is_value = form.getFieldValue('auth');
          if (type === "form" && !is_value) {
            form.setFieldsValue({'auth': false});
          }
          return <Switch checked={is_value} onClick={(checked) => {
            form.setFieldsValue({'auth': checked});
          }} />;
        },
                                },{
                      title: '路由关联的页面组件',
                      dataIndex: 'component',
                      rules: [
                        {
                          required: true,
                          message: '路由关联的页面组件为必填项',
                        },
                      ],
                    },{
                              title: '路由关联权限',
                              dataIndex: 'permission',
                              backendType: 'foreignKey',
                              rules: [
                                {
                                  required: true,
                                  message: '路由关联权限为必填项',
                                },
                              ],
                                    renderFormItem: (item, {value, onChange}) => {
            const children = permissionForeignKeyList.map((item) => {
              return <Option key={item.id} value={item.id}>{item.name}</Option>;
            });
            return <Select
              placeholder="请选择路由关联权限"
              onChange={onChange}
            >
              {children}
            </Select>;
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
                                    
                                    handleUpdateModalVisible(true);
                                    setUpdateFormValues(record);
                                  }} />
                                  <Divider type="vertical" />
                                  <Popconfirm
                                    title="您确定要删除用户路由吗？"
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

  const [permissionForeignKeyList, setPermissionForeignKeyList] = useState([]);
      useEffect(() => {
        queryPermission().then(value => {
          setPermissionForeignKeyList(value.data);
        });
      }, []);


    
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
        headerTitle="用户路由表格"
        actionRef={actionRef}
        rowKey="id"
        toolBarRender={(action, {selectedRows}) => [
          <Button type="primary" onClick={() => handleModalVisible(true)}>
            <PlusOutlined /> 新建
          </Button>,
          <Input.Search style={{marginRight: 20}} placeholder="搜索用户路由 " onSearch={value => {
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
        request={(params, sorter, filter) => queryUserRouter({...params, sorter, filter})}
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
