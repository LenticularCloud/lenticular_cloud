from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.plugin_config_args import PluginConfigArgs
from ..models.plugin_config_interface import PluginConfigInterface
from ..models.plugin_config_linux import PluginConfigLinux
from ..models.plugin_config_network import PluginConfigNetwork
from ..models.plugin_config_rootfs import PluginConfigRootfs
from ..models.plugin_config_user import PluginConfigUser
from ..models.plugin_env import PluginEnv
from ..models.plugin_mount import PluginMount
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginConfig")


@attr.s(auto_attribs=True)
class PluginConfig:
    """
    Attributes:
        args (PluginConfigArgs): PluginConfigArgs plugin config args
        description (str): description
        documentation (str): documentation
        entrypoint (List[str]): entrypoint
        env (List[PluginEnv]): env
        interface (PluginConfigInterface): PluginConfigInterface The interface between Docker and the plugin
        ipc_host (bool): ipc host
        linux (PluginConfigLinux): PluginConfigLinux plugin config linux
        mounts (List[PluginMount]): mounts
        network (PluginConfigNetwork): PluginConfigNetwork plugin config network
        pid_host (bool): pid host
        propagated_mount (str): propagated mount
        work_dir (str): work dir
        docker_version (Union[Unset, str]): Docker Version used to create the plugin
        user (Union[Unset, PluginConfigUser]): PluginConfigUser plugin config user
        rootfs (Union[Unset, PluginConfigRootfs]): PluginConfigRootfs plugin config rootfs
    """

    args: PluginConfigArgs
    description: str
    documentation: str
    entrypoint: List[str]
    env: List[PluginEnv]
    interface: PluginConfigInterface
    ipc_host: bool
    linux: PluginConfigLinux
    mounts: List[PluginMount]
    network: PluginConfigNetwork
    pid_host: bool
    propagated_mount: str
    work_dir: str
    docker_version: Union[Unset, str] = UNSET
    user: Union[Unset, PluginConfigUser] = UNSET
    rootfs: Union[Unset, PluginConfigRootfs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        args = self.args.to_dict()

        description = self.description
        documentation = self.documentation
        entrypoint = self.entrypoint

        env = []
        for env_item_data in self.env:
            env_item = env_item_data.to_dict()

            env.append(env_item)

        interface = self.interface.to_dict()

        ipc_host = self.ipc_host
        linux = self.linux.to_dict()

        mounts = []
        for mounts_item_data in self.mounts:
            mounts_item = mounts_item_data.to_dict()

            mounts.append(mounts_item)

        network = self.network.to_dict()

        pid_host = self.pid_host
        propagated_mount = self.propagated_mount
        work_dir = self.work_dir
        docker_version = self.docker_version
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        rootfs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rootfs, Unset):
            rootfs = self.rootfs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Args": args,
                "Description": description,
                "Documentation": documentation,
                "Entrypoint": entrypoint,
                "Env": env,
                "Interface": interface,
                "IpcHost": ipc_host,
                "Linux": linux,
                "Mounts": mounts,
                "Network": network,
                "PidHost": pid_host,
                "PropagatedMount": propagated_mount,
                "WorkDir": work_dir,
            }
        )
        if docker_version is not UNSET:
            field_dict["DockerVersion"] = docker_version
        if user is not UNSET:
            field_dict["User"] = user
        if rootfs is not UNSET:
            field_dict["rootfs"] = rootfs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        args = PluginConfigArgs.from_dict(_d.pop("Args"))

        description = _d.pop("Description")

        documentation = _d.pop("Documentation")

        entrypoint = cast(List[str], _d.pop("Entrypoint"))

        env = []
        _env = _d.pop("Env")
        for env_item_data in _env:
            env_item = PluginEnv.from_dict(env_item_data)

            env.append(env_item)

        interface = PluginConfigInterface.from_dict(_d.pop("Interface"))

        ipc_host = _d.pop("IpcHost")

        linux = PluginConfigLinux.from_dict(_d.pop("Linux"))

        mounts = []
        _mounts = _d.pop("Mounts")
        for mounts_item_data in _mounts:
            mounts_item = PluginMount.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        network = PluginConfigNetwork.from_dict(_d.pop("Network"))

        pid_host = _d.pop("PidHost")

        propagated_mount = _d.pop("PropagatedMount")

        work_dir = _d.pop("WorkDir")

        docker_version = _d.pop("DockerVersion", UNSET)

        _user = _d.pop("User", UNSET)
        user: Union[Unset, PluginConfigUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PluginConfigUser.from_dict(_user)

        _rootfs = _d.pop("rootfs", UNSET)
        rootfs: Union[Unset, PluginConfigRootfs]
        if isinstance(_rootfs, Unset):
            rootfs = UNSET
        else:
            rootfs = PluginConfigRootfs.from_dict(_rootfs)

        plugin_config = cls(
            args=args,
            description=description,
            documentation=documentation,
            entrypoint=entrypoint,
            env=env,
            interface=interface,
            ipc_host=ipc_host,
            linux=linux,
            mounts=mounts,
            network=network,
            pid_host=pid_host,
            propagated_mount=propagated_mount,
            work_dir=work_dir,
            docker_version=docker_version,
            user=user,
            rootfs=rootfs,
        )

        plugin_config.additional_properties = _d
        return plugin_config

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
