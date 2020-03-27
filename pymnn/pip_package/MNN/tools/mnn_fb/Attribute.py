# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Attribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAttribute(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Attribute()
        x.Init(buf, n + offset)
        return x

    # Attribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Attribute
    def S(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Attribute
    def I(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Attribute
    def B(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Attribute
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Attribute
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Attribute
    def F(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Attribute
    def Tensor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Blob import Blob
            obj = Blob()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Attribute
    def List(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ListValue import ListValue
            obj = ListValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def AttributeStart(builder): builder.StartObject(8)
def AttributeAddS(builder, s): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(s), 0)
def AttributeAddI(builder, i): builder.PrependInt32Slot(1, i, 0)
def AttributeAddB(builder, b): builder.PrependBoolSlot(2, b, 0)
def AttributeAddKey(builder, key): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)
def AttributeAddType(builder, type): builder.PrependInt32Slot(4, type, 0)
def AttributeAddF(builder, f): builder.PrependFloat32Slot(5, f, 0.0)
def AttributeAddTensor(builder, tensor): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(tensor), 0)
def AttributeAddList(builder, list): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(list), 0)
def AttributeEnd(builder): return builder.EndObject()
