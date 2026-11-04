"""Upload proven, separately generated DB2 COPY members before COBOL members.

A generated program must never be uploaded while the COPY members it needs
are merely local files. The destination PDS is explicit and separate from the
program library; never default to the source copybook dataset.
"""
from __future__ import annotations

from pathlib import Path

from mainframe.zowe_client import ZoweClient
from mainframe.zowe_env import raw_setting
from mainframe.zowe_settings import build_output_profile, expand

DATASET_SETTING = 'ZOWE_GENERATED_COPYBOOK_DATASET'


def staging_directory(output_dir: Path) -> Path:
    return output_dir / 'Generated Copybooks'


def require_copybook_upload_configuration(output_dir: Path) -> tuple[Path, ...]:
    members = tuple(sorted(staging_directory(output_dir).glob('*.cpy')))
    if members and not raw_setting(DATASET_SETTING, '').strip():
        raise ValueError(
            f'{len(members)} derived DB2 COPY member(s) require an explicit '
            f'{DATASET_SETTING}. No program upload is allowed until the '
            'converted COPY assets have a configured target PDS.'
        )
    names = [member.stem.upper() for member in members]
    if len(names) != len(set(names)) or any(len(name) > 8 or not name.isalnum() for name in names):
        raise ValueError('generated copybook members contain unsafe/duplicate PDS names')
    return members


def upload_generated_copybooks(output_dir: Path, diagnostics: list[str]) -> None:
    members = require_copybook_upload_configuration(output_dir)
    if not members:
        return
    profile = build_output_profile()
    destination = expand(raw_setting(DATASET_SETTING, ''))
    client = ZoweClient(profile.connection, profile.key, 'Generated DB2 copybooks')
    for member in members:
        payload = member.read_bytes()
        client.upload_member(destination, member.stem.upper(), payload)
        client.verify_member(destination, member.stem.upper(), payload)
        diagnostics.append(f'Verified COPY {destination}({member.stem.upper()})')
