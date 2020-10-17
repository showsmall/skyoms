import request from '@/plugin/axios'
export function  getcluster(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/cluster/',
    method: 'get',
    params
  })
}

export function  getdatacenter(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/datacenter/',
    method: 'get',
    params
  })
}
export function  getdatastore(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/datastore/',
    method: 'get',
    params
  })
}
export function  getnetworkadapter(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/networkadapter/',
    method: 'get',
    params
  })
}
export function  getdedicatedhost(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/dedicatedhost/',
    method: 'get',
    params
  })
}

export function  getvirtualhost(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/virtualhost/',
    method: 'get',
    params
  })
}
export function  getclusterhost(params) {
  return request ({
    url: process.env.VUE_APP_BASE_API + '/vms/getclusterhost/',
    method: 'get',
    params
  })
}

