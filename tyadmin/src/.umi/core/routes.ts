// @ts-nocheck
import { ApplyPluginsType, dynamic } from '/Users/carlos/Desktop/my_pro/skyoms/tyadmin/node_modules/@umijs/runtime';
import { plugin } from './plugin';

const routes = [
  {
    "path": "/xadmin/login",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__UserLayout' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/layouts/UserLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "name": "login",
        "path": "/xadmin/login",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__UserLogin' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/UserLogin'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "path": "/xadmin/",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__SecurityLayout' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/layouts/SecurityLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "path": "/xadmin/",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__BasicLayout' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/layouts/BasicLayout'), loading: require('@/components/PageLoading/index').default}),
        "authority": [
          "admin",
          "user"
        ],
        "routes": [
          {
            "name": "首页",
            "path": "/xadmin/index",
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__DashBoard' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/DashBoard'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "path": "/xadmin/",
            "redirect": "/xadmin/index",
            "exact": true
          },
          {
            "name": "首页",
            "path": "/xadmin/index",
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__DashBoard' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/DashBoard'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "用户菜单",
            "icon": "smile",
            "path": "/xadmin/user_menu",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserMenuList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/UserMenuList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "用户路由",
            "icon": "smile",
            "path": "/xadmin/user_router",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserRouterList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/UserRouterList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "用户表",
            "icon": "smile",
            "path": "/xadmin/user_profile",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserProfileList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/UserProfileList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "数据中心",
            "icon": "smile",
            "path": "/xadmin/data_centers",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__DataCentersList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/DataCentersList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "集群",
            "icon": "smile",
            "path": "/xadmin/clusters",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__ClustersList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/ClustersList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "存储",
            "icon": "smile",
            "path": "/xadmin/data_stores",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__DataStoresList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/DataStoresList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "网络端口",
            "icon": "smile",
            "path": "/xadmin/network_adapters",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__NetworkAdaptersList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/NetworkAdaptersList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "宿主机",
            "icon": "smile",
            "path": "/xadmin/dedicatedhosts",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__DedicatedhostsList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/DedicatedhostsList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "虚拟机",
            "icon": "smile",
            "path": "/xadmin/virtual_hosts",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__VirtualHostsList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/VirtualHostsList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "机房",
            "icon": "smile",
            "path": "/xadmin/i_d_c",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__IDCList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/IDCList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "主机",
            "icon": "smile",
            "path": "/xadmin/hosts",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__HostsList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/HostsList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "主机组",
            "icon": "smile",
            "path": "/xadmin/host_group",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__HostGroupList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/AutoGenPage/HostGroupList'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "name": "Tyadmin内置",
            "icon": "VideoCamera",
            "path": "/xadmin/sys",
            "routes": [
              {
                "name": "TyAdmin日志",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminSysLogList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdmin验证",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminEmailVerifyRecordList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "Tyadmin内置",
            "icon": "VideoCamera",
            "path": "/xadmin/sys",
            "routes": [
              {
                "name": "TyAdmin日志",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminSysLogList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdmin验证",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminEmailVerifyRecordList' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/TyAdminBuiltIn/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          }
        ]
      },
      {
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/Users/carlos/Desktop/my_pro/skyoms/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
    "exact": true
  }
];

// allow user to extend routes
plugin.applyPlugins({
  key: 'patchRoutes',
  type: ApplyPluginsType.event,
  args: { routes },
});

export { routes };
