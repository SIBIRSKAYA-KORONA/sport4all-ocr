# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ocr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='ocr.proto',
    package='proto',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\tocr.proto\x12\x05proto\"B\n\x05Image\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x15\n\rplayer_column\x18\x02 \x01(\x05\x12\x14\n\x0cscore_column\x18\x03 \x01(\x05\":\n\nPlayerStat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\"w\n\x0bPlayerStats\x12,\n\x05stats\x18\x01 \x03(\x0b\x32\x1d.proto.PlayerStats.PlayerStat\x1a:\n\nPlayerStat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x32\x41\n\nOcrService\x12\x33\n\x0fGetStatsByImage\x12\x0c.proto.Image\x1a\x12.proto.PlayerStatsb\x06proto3'
)


_IMAGE = _descriptor.Descriptor(
    name='Image',
    full_name='proto.Image',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='link', full_name='proto.Image.link', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='player_column', full_name='proto.Image.player_column', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='score_column', full_name='proto.Image.score_column', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=20,
    serialized_end=86,
)


_PLAYERSTAT = _descriptor.Descriptor(
    name='PlayerStat',
    full_name='proto.PlayerStat',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='proto.PlayerStat.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='surname', full_name='proto.PlayerStat.surname', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='score', full_name='proto.PlayerStat.score', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=88,
    serialized_end=146,
)


_PLAYERSTATS_PLAYERSTAT = _descriptor.Descriptor(
    name='PlayerStat',
    full_name='proto.PlayerStats.PlayerStat',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='proto.PlayerStats.PlayerStat.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='surname', full_name='proto.PlayerStats.PlayerStat.surname', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='score', full_name='proto.PlayerStats.PlayerStat.score', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=88,
    serialized_end=146,
)

_PLAYERSTATS = _descriptor.Descriptor(
    name='PlayerStats',
    full_name='proto.PlayerStats',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='stats', full_name='proto.PlayerStats.stats', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[_PLAYERSTATS_PLAYERSTAT, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=148,
    serialized_end=267,
)

_PLAYERSTATS_PLAYERSTAT.containing_type = _PLAYERSTATS
_PLAYERSTATS.fields_by_name['stats'].message_type = _PLAYERSTATS_PLAYERSTAT
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['PlayerStat'] = _PLAYERSTAT
DESCRIPTOR.message_types_by_name['PlayerStats'] = _PLAYERSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
    'DESCRIPTOR': _IMAGE,
    '__module__': 'ocr_pb2'
    # @@protoc_insertion_point(class_scope:proto.Image)
})
_sym_db.RegisterMessage(Image)

PlayerStat = _reflection.GeneratedProtocolMessageType('PlayerStat', (_message.Message,), {
    'DESCRIPTOR': _PLAYERSTAT,
    '__module__': 'ocr_pb2'
    # @@protoc_insertion_point(class_scope:proto.PlayerStat)
})
_sym_db.RegisterMessage(PlayerStat)

PlayerStats = _reflection.GeneratedProtocolMessageType('PlayerStats', (_message.Message,), {

    'PlayerStat': _reflection.GeneratedProtocolMessageType('PlayerStat', (_message.Message,), {
        'DESCRIPTOR': _PLAYERSTATS_PLAYERSTAT,
        '__module__': 'ocr_pb2'
        # @@protoc_insertion_point(class_scope:proto.PlayerStats.PlayerStat)
    }),
    'DESCRIPTOR': _PLAYERSTATS,
    '__module__': 'ocr_pb2'
    # @@protoc_insertion_point(class_scope:proto.PlayerStats)
})
_sym_db.RegisterMessage(PlayerStats)
_sym_db.RegisterMessage(PlayerStats.PlayerStat)


_OCRSERVICE = _descriptor.ServiceDescriptor(
    name='OcrService',
    full_name='proto.OcrService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=269,
    serialized_end=334,
    methods=[
        _descriptor.MethodDescriptor(
            name='GetStatsByImage',
            full_name='proto.OcrService.GetStatsByImage',
            index=0,
            containing_service=None,
            input_type=_IMAGE,
            output_type=_PLAYERSTATS,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_OCRSERVICE)

DESCRIPTOR.services_by_name['OcrService'] = _OCRSERVICE

# @@protoc_insertion_point(module_scope)
