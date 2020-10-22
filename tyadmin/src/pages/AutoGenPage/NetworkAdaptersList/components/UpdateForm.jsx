import React from 'react';
import {Modal} from 'antd';

const UpdateForm = props => {
  const {modalVisible, onCancel} = props;
  return (
    <Modal
      destroyOnClose
      title="修改网络端口"
      visible={modalVisible}
      width={600}
      onCancel={() => onCancel()}
      footer={null}
    >
      {props.children}
    </Modal>
  );
};

export default UpdateForm;
