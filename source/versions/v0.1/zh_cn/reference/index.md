# 参考资料

本节包含 MuduDB 的稳定参考资料。

```{toctree}
:maxdepth: 2

contracts/index
mcli-admin
```

## 格式与协议契约

持久化格式、网络协议与部署制品的正式版本化规范。

- [Page Header 契约 v1](contracts/page_header_v1.md)
- [Tuple Binary Format 契约 v1](contracts/tuple_binary_v1.md)
- [Log Frame 契约 v1](contracts/log_frame_v1.md)
- [TCP 协议帧契约 v1](contracts/protocol_frame_v1.md)
- [MPK 包清单契约 v1](contracts/mpk_manifest_v1.md)
- [服务端配置契约 v1](contracts/mudud_cfg_v1.md)
- [文件布局契约 v1](contracts/file_layout_v1.md)
- [Guest→Host 系统调用负载契约 v1](contracts/syscall_payload_v1.md)
- [如何添加一次格式升级](contracts/how_to_add_format_upgrade.md)

## 运维管理

运维命令与接口参考。

- [mcli HTTP 管理接口](mcli-admin.md)
