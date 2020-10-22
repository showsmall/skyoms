import request from 'umi-request';

export async function queryHostGroup(params) {
  return request('/api/xadmin/v1/host_group', {
    params,
  });
}
export async function removeHostGroup(params) {
  return request(`/api/xadmin/v1/host_group/${params}`, {
    method: 'DELETE',
  });
}
export async function addHostGroup(params) {
  return request('/api/xadmin/v1/host_group', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateHostGroup(params, id) {
  return request(`/api/xadmin/v1/host_group/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
