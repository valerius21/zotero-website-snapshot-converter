from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Meta:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        return Meta()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Data:
    key: Optional[str] = None
    version: Optional[int] = None
    parent_item: Optional[str] = None
    item_type: Optional[str] = None
    link_mode: Optional[str] = None
    title: Optional[str] = None
    access_date: Optional[datetime] = None
    url: Optional[str] = None
    note: Optional[str] = None
    content_type: Optional[str] = None
    charset: Optional[str] = None
    filename: Optional[str] = None
    md5: Optional[str] = None
    mtime: Optional[int] = None
    tags: Optional[List[Any]] = None
    relations: Optional[Meta] = None
    date_added: Optional[datetime] = None
    date_modified: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        version = from_union([from_int, from_none], obj.get("version"))
        parent_item = from_union([from_str, from_none], obj.get("parentItem"))
        item_type = from_union([from_str, from_none], obj.get("itemType"))
        link_mode = from_union([from_str, from_none], obj.get("linkMode"))
        title = from_union([from_str, from_none], obj.get("title"))
        access_date = from_union([from_datetime, from_none], obj.get("accessDate"))
        url = from_union([from_str, from_none], obj.get("url"))
        note = from_union([from_str, from_none], obj.get("note"))
        content_type = from_union([from_str, from_none], obj.get("contentType"))
        charset = from_union([from_str, from_none], obj.get("charset"))
        filename = from_union([from_str, from_none], obj.get("filename"))
        md5 = from_union([from_str, from_none], obj.get("md5"))
        mtime = from_union([from_int, from_none], obj.get("mtime"))
        tags = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("tags"))
        relations = from_union([Meta.from_dict, from_none], obj.get("relations"))
        date_added = from_union([from_datetime, from_none], obj.get("dateAdded"))
        date_modified = from_union([from_datetime, from_none], obj.get("dateModified"))
        return Data(key, version, parent_item, item_type, link_mode, title, access_date, url, note, content_type,
                    charset, filename, md5, mtime, tags, relations, date_added, date_modified)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.version is not None:
            result["version"] = from_union([from_int, from_none], self.version)
        if self.parent_item is not None:
            result["parentItem"] = from_union([from_str, from_none], self.parent_item)
        if self.item_type is not None:
            result["itemType"] = from_union([from_str, from_none], self.item_type)
        if self.link_mode is not None:
            result["linkMode"] = from_union([from_str, from_none], self.link_mode)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.access_date is not None:
            result["accessDate"] = from_union([lambda x: x.isoformat(), from_none], self.access_date)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.note is not None:
            result["note"] = from_union([from_str, from_none], self.note)
        if self.content_type is not None:
            result["contentType"] = from_union([from_str, from_none], self.content_type)
        if self.charset is not None:
            result["charset"] = from_union([from_str, from_none], self.charset)
        if self.filename is not None:
            result["filename"] = from_union([from_str, from_none], self.filename)
        if self.md5 is not None:
            result["md5"] = from_union([from_str, from_none], self.md5)
        if self.mtime is not None:
            result["mtime"] = from_union([from_int, from_none], self.mtime)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.tags)
        if self.relations is not None:
            result["relations"] = from_union([lambda x: to_class(Meta, x), from_none], self.relations)
        if self.date_added is not None:
            result["dateAdded"] = from_union([lambda x: x.isoformat(), from_none], self.date_added)
        if self.date_modified is not None:
            result["dateModified"] = from_union([lambda x: x.isoformat(), from_none], self.date_modified)
        return result


@dataclass
class Alternate:
    href: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Alternate':
        assert isinstance(obj, dict)
        href = from_union([from_str, from_none], obj.get("href"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Alternate(href, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.href is not None:
            result["href"] = from_union([from_str, from_none], self.href)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class LibraryLinks:
    alternate: Optional[Alternate] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LibraryLinks':
        assert isinstance(obj, dict)
        alternate = from_union([Alternate.from_dict, from_none], obj.get("alternate"))
        return LibraryLinks(alternate)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.alternate is not None:
            result["alternate"] = from_union([lambda x: to_class(Alternate, x), from_none], self.alternate)
        return result


@dataclass
class Library:
    type: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    links: Optional[LibraryLinks] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Library':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        links = from_union([LibraryLinks.from_dict, from_none], obj.get("links"))
        return Library(type, id, name, links)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.links is not None:
            result["links"] = from_union([lambda x: to_class(LibraryLinks, x), from_none], self.links)
        return result


@dataclass
class AttachmentResponseLinks:
    links_self: Optional[Alternate] = None
    alternate: Optional[Alternate] = None
    up: Optional[Alternate] = None
    enclosure: Optional[Alternate] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AttachmentResponseLinks':
        assert isinstance(obj, dict)
        links_self = from_union([Alternate.from_dict, from_none], obj.get("self"))
        alternate = from_union([Alternate.from_dict, from_none], obj.get("alternate"))
        up = from_union([Alternate.from_dict, from_none], obj.get("up"))
        enclosure = from_union([Alternate.from_dict, from_none], obj.get("enclosure"))
        return AttachmentResponseLinks(links_self, alternate, up, enclosure)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.links_self is not None:
            result["self"] = from_union([lambda x: to_class(Alternate, x), from_none], self.links_self)
        if self.alternate is not None:
            result["alternate"] = from_union([lambda x: to_class(Alternate, x), from_none], self.alternate)
        if self.up is not None:
            result["up"] = from_union([lambda x: to_class(Alternate, x), from_none], self.up)
        if self.enclosure is not None:
            result["enclosure"] = from_union([lambda x: to_class(Alternate, x), from_none], self.enclosure)
        return result


@dataclass
class AttachmentResponse:
    key: Optional[str] = None
    version: Optional[int] = None
    library: Optional[Library] = None
    links: Optional[AttachmentResponseLinks] = None
    meta: Optional[Meta] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AttachmentResponse':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        version = from_union([from_int, from_none], obj.get("version"))
        library = from_union([Library.from_dict, from_none], obj.get("library"))
        links = from_union([AttachmentResponseLinks.from_dict, from_none], obj.get("links"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AttachmentResponse(key, version, library, links, meta, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.version is not None:
            result["version"] = from_union([from_int, from_none], self.version)
        if self.library is not None:
            result["library"] = from_union([lambda x: to_class(Library, x), from_none], self.library)
        if self.links is not None:
            result["links"] = from_union([lambda x: to_class(AttachmentResponseLinks, x), from_none], self.links)
        if self.meta is not None:
            result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def attachment_response_from_dict(s: Any) -> AttachmentResponse:
    return AttachmentResponse.from_dict(s)


def attachment_response_to_dict(x: AttachmentResponse) -> Any:
    return to_class(AttachmentResponse, x)
