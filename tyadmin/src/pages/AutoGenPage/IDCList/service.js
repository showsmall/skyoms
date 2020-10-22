import request from 'umi-request';

export async function queryIDC(params) {
  return request('/api/xadmin/v1/i_d_c', {
    params,
  });
}
export async function removeIDC(params) {
  return request(`/api/xadmin/v1/i_d_c/${params}`, {
    method: 'DELETE',
  });
}
export async function addIDC(params) {
  return request('/api/xadmin/v1/i_d_c', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateIDC(params, id) {
  return request(`/api/xadmin/v1/i_d_c/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
