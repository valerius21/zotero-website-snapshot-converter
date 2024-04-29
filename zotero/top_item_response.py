from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, Union, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


class Collection(Enum):
    M88_J9_DDU = "M88J9DDU"
    ZDBM3_ULJ = "ZDBM3ULJ"


class CreatorType(Enum):
    AUTHOR = "author"
    EDITOR = "editor"
    PROGRAMMER = "programmer"


@dataclass
class Creator:
    creator_type: Optional[CreatorType] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Creator':
        assert isinstance(obj, dict)
        creator_type = from_union([CreatorType, from_none], obj.get("creatorType"))
        first_name = from_union([from_str, from_none], obj.get("firstName"))
        last_name = from_union([from_str, from_none], obj.get("lastName"))
        return Creator(creator_type, first_name, last_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.creator_type is not None:
            result["creatorType"] = from_union([lambda x: to_enum(CreatorType, x), from_none], self.creator_type)
        if self.first_name is not None:
            result["firstName"] = from_union([from_str, from_none], self.first_name)
        if self.last_name is not None:
            result["lastName"] = from_union([from_str, from_none], self.last_name)
        return result


class Language(Enum):
    EMPTY = ""
    EN = "en"
    EN_US = "en-US"
    LANGUAGE_EN_US = "en-us"


@dataclass
class Relations:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Relations':
        assert isinstance(obj, dict)
        return Relations()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Tag:
    tag: Optional[str] = None
    type: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        assert isinstance(obj, dict)
        tag = from_union([from_str, from_none], obj.get("tag"))
        type = from_union([from_int, from_none], obj.get("type"))
        return Tag(tag, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.tag is not None:
            result["tag"] = from_union([from_str, from_none], self.tag)
        if self.type is not None:
            result["type"] = from_union([from_int, from_none], self.type)
        return result


@dataclass
class Data:
    key: Optional[str] = None
    version: Optional[int] = None
    item_type: Optional[str] = None
    title: Optional[str] = None
    creators: Optional[List[Creator]] = None
    abstract_note: Optional[str] = None
    website_title: Optional[str] = None
    website_type: Optional[str] = None
    date: Optional[str] = None
    short_title: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    language: Optional[Language] = None
    rights: Optional[str] = None
    extra: Optional[str] = None
    tags: Optional[List[Tag]] = None
    collections: Optional[List[Collection]] = None
    relations: Optional[Relations] = None
    date_added: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    blog_title: Optional[str] = None
    publication_title: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    series: Optional[str] = None
    series_title: Optional[str] = None
    series_text: Optional[str] = None
    journal_abbreviation: Optional[str] = None
    doi: Optional[str] = None
    issn: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    version_number: Optional[str] = None
    system: Optional[str] = None
    place: Optional[str] = None
    company: Optional[str] = None
    programming_language: Optional[str] = None
    isbn: Optional[str] = None
    proceedings_title: Optional[str] = None
    conference_name: Optional[str] = None
    publisher: Optional[str] = None
    identifier: Optional[str] = None
    type: Optional[str] = None
    repository: Optional[str] = None
    repository_location: Optional[str] = None
    format: Optional[str] = None
    citation_key: Optional[str] = None
    genre: Optional[str] = None
    archive_id: Optional[str] = None
    series_number: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        version = from_union([from_int, from_none], obj.get("version"))
        item_type = from_union([from_str, from_none], obj.get("itemType"))
        title = from_union([from_str, from_none], obj.get("title"))
        creators = from_union([lambda x: from_list(Creator.from_dict, x), from_none], obj.get("creators"))
        abstract_note = from_union([from_str, from_none], obj.get("abstractNote"))
        website_title = from_union([from_str, from_none], obj.get("websiteTitle"))
        website_type = from_union([from_str, from_none], obj.get("websiteType"))
        date = from_union([from_str, from_none], obj.get("date"))
        short_title = from_union([from_str, from_none], obj.get("shortTitle"))
        url = from_union([from_str, from_none], obj.get("url"))
        access_date = from_union([from_str, from_none], obj.get("accessDate"))
        language = from_union([Language, from_none], obj.get("language"))
        rights = from_union([from_str, from_none], obj.get("rights"))
        extra = from_union([from_str, from_none], obj.get("extra"))
        tags = from_union([lambda x: from_list(Tag.from_dict, x), from_none], obj.get("tags"))
        collections = from_union([lambda x: from_list(Collection, x), from_none], obj.get("collections"))
        relations = from_union([Relations.from_dict, from_none], obj.get("relations"))
        date_added = from_union([from_datetime, from_none], obj.get("dateAdded"))
        date_modified = from_union([from_datetime, from_none], obj.get("dateModified"))
        blog_title = from_union([from_str, from_none], obj.get("blogTitle"))
        publication_title = from_union([from_str, from_none], obj.get("publicationTitle"))
        volume = from_union([from_str, from_none], obj.get("volume"))
        issue = from_union([from_str, from_none], obj.get("issue"))
        pages = from_union([from_str, from_none], obj.get("pages"))
        series = from_union([from_str, from_none], obj.get("series"))
        series_title = from_union([from_str, from_none], obj.get("seriesTitle"))
        series_text = from_union([from_str, from_none], obj.get("seriesText"))
        journal_abbreviation = from_union([from_str, from_none], obj.get("journalAbbreviation"))
        doi = from_union([from_str, from_none], obj.get("DOI"))
        issn = from_union([from_str, from_none], obj.get("ISSN"))
        archive = from_union([from_str, from_none], obj.get("archive"))
        archive_location = from_union([from_str, from_none], obj.get("archiveLocation"))
        library_catalog = from_union([from_str, from_none], obj.get("libraryCatalog"))
        call_number = from_union([from_str, from_none], obj.get("callNumber"))
        version_number = from_union([from_str, from_none], obj.get("versionNumber"))
        system = from_union([from_str, from_none], obj.get("system"))
        place = from_union([from_str, from_none], obj.get("place"))
        company = from_union([from_str, from_none], obj.get("company"))
        programming_language = from_union([from_str, from_none], obj.get("programmingLanguage"))
        isbn = from_union([from_str, from_none], obj.get("ISBN"))
        proceedings_title = from_union([from_str, from_none], obj.get("proceedingsTitle"))
        conference_name = from_union([from_str, from_none], obj.get("conferenceName"))
        publisher = from_union([from_str, from_none], obj.get("publisher"))
        identifier = from_union([from_str, from_none], obj.get("identifier"))
        type = from_union([from_str, from_none], obj.get("type"))
        repository = from_union([from_str, from_none], obj.get("repository"))
        repository_location = from_union([from_str, from_none], obj.get("repositoryLocation"))
        format = from_union([from_str, from_none], obj.get("format"))
        citation_key = from_union([from_str, from_none], obj.get("citationKey"))
        genre = from_union([from_str, from_none], obj.get("genre"))
        archive_id = from_union([from_str, from_none], obj.get("archiveID"))
        series_number = from_union([from_str, from_none], obj.get("seriesNumber"))
        return Data(key, version, item_type, title, creators, abstract_note, website_title, website_type, date,
                    short_title, url, access_date, language, rights, extra, tags, collections, relations, date_added,
                    date_modified, blog_title, publication_title, volume, issue, pages, series, series_title,
                    series_text, journal_abbreviation, doi, issn, archive, archive_location, library_catalog,
                    call_number, version_number, system, place, company, programming_language, isbn, proceedings_title,
                    conference_name, publisher, identifier, type, repository, repository_location, format, citation_key,
                    genre, archive_id, series_number)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.version is not None:
            result["version"] = from_union([from_int, from_none], self.version)
        if self.item_type is not None:
            result["itemType"] = from_union([from_str, from_none], self.item_type)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.creators is not None:
            result["creators"] = from_union([lambda x: from_list(lambda x: to_class(Creator, x), x), from_none],
                                            self.creators)
        if self.abstract_note is not None:
            result["abstractNote"] = from_union([from_str, from_none], self.abstract_note)
        if self.website_title is not None:
            result["websiteTitle"] = from_union([from_str, from_none], self.website_title)
        if self.website_type is not None:
            result["websiteType"] = from_union([from_str, from_none], self.website_type)
        if self.date is not None:
            result["date"] = from_union([from_str, from_none], self.date)
        if self.short_title is not None:
            result["shortTitle"] = from_union([from_str, from_none], self.short_title)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.access_date is not None:
            result["accessDate"] = from_union([from_str, from_none], self.access_date)
        if self.language is not None:
            result["language"] = from_union([lambda x: to_enum(Language, x), from_none], self.language)
        if self.rights is not None:
            result["rights"] = from_union([from_str, from_none], self.rights)
        if self.extra is not None:
            result["extra"] = from_union([from_str, from_none], self.extra)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(lambda x: to_class(Tag, x), x), from_none], self.tags)
        if self.collections is not None:
            result["collections"] = from_union([lambda x: from_list(lambda x: to_enum(Collection, x), x), from_none],
                                               self.collections)
        if self.relations is not None:
            result["relations"] = from_union([lambda x: to_class(Relations, x), from_none], self.relations)
        if self.date_added is not None:
            result["dateAdded"] = from_union([lambda x: x.isoformat(), from_none], self.date_added)
        if self.date_modified is not None:
            result["dateModified"] = from_union([lambda x: x.isoformat(), from_none], self.date_modified)
        if self.blog_title is not None:
            result["blogTitle"] = from_union([from_str, from_none], self.blog_title)
        if self.publication_title is not None:
            result["publicationTitle"] = from_union([from_str, from_none], self.publication_title)
        if self.volume is not None:
            result["volume"] = from_union([from_str, from_none], self.volume)
        if self.issue is not None:
            result["issue"] = from_union([from_str, from_none], self.issue)
        if self.pages is not None:
            result["pages"] = from_union([from_str, from_none], self.pages)
        if self.series is not None:
            result["series"] = from_union([from_str, from_none], self.series)
        if self.series_title is not None:
            result["seriesTitle"] = from_union([from_str, from_none], self.series_title)
        if self.series_text is not None:
            result["seriesText"] = from_union([from_str, from_none], self.series_text)
        if self.journal_abbreviation is not None:
            result["journalAbbreviation"] = from_union([from_str, from_none], self.journal_abbreviation)
        if self.doi is not None:
            result["DOI"] = from_union([from_str, from_none], self.doi)
        if self.issn is not None:
            result["ISSN"] = from_union([from_str, from_none], self.issn)
        if self.archive is not None:
            result["archive"] = from_union([from_str, from_none], self.archive)
        if self.archive_location is not None:
            result["archiveLocation"] = from_union([from_str, from_none], self.archive_location)
        if self.library_catalog is not None:
            result["libraryCatalog"] = from_union([from_str, from_none], self.library_catalog)
        if self.call_number is not None:
            result["callNumber"] = from_union([from_str, from_none], self.call_number)
        if self.version_number is not None:
            result["versionNumber"] = from_union([from_str, from_none], self.version_number)
        if self.system is not None:
            result["system"] = from_union([from_str, from_none], self.system)
        if self.place is not None:
            result["place"] = from_union([from_str, from_none], self.place)
        if self.company is not None:
            result["company"] = from_union([from_str, from_none], self.company)
        if self.programming_language is not None:
            result["programmingLanguage"] = from_union([from_str, from_none], self.programming_language)
        if self.isbn is not None:
            result["ISBN"] = from_union([from_str, from_none], self.isbn)
        if self.proceedings_title is not None:
            result["proceedingsTitle"] = from_union([from_str, from_none], self.proceedings_title)
        if self.conference_name is not None:
            result["conferenceName"] = from_union([from_str, from_none], self.conference_name)
        if self.publisher is not None:
            result["publisher"] = from_union([from_str, from_none], self.publisher)
        if self.identifier is not None:
            result["identifier"] = from_union([from_str, from_none], self.identifier)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.repository is not None:
            result["repository"] = from_union([from_str, from_none], self.repository)
        if self.repository_location is not None:
            result["repositoryLocation"] = from_union([from_str, from_none], self.repository_location)
        if self.format is not None:
            result["format"] = from_union([from_str, from_none], self.format)
        if self.citation_key is not None:
            result["citationKey"] = from_union([from_str, from_none], self.citation_key)
        if self.genre is not None:
            result["genre"] = from_union([from_str, from_none], self.genre)
        if self.archive_id is not None:
            result["archiveID"] = from_union([from_str, from_none], self.archive_id)
        if self.series_number is not None:
            result["seriesNumber"] = from_union([from_str, from_none], self.series_number)
        return result


class AlternateType(Enum):
    APPLICATION_JSON = "application/json"
    TEXT_HTML = "text/html"


@dataclass
class Alternate:
    href: Optional[str] = None
    type: Optional[AlternateType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Alternate':
        assert isinstance(obj, dict)
        href = from_union([from_str, from_none], obj.get("href"))
        type = from_union([AlternateType, from_none], obj.get("type"))
        return Alternate(href, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.href is not None:
            result["href"] = from_union([from_str, from_none], self.href)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(AlternateType, x), from_none], self.type)
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


class LibraryType(Enum):
    USER = "user"


@dataclass
class Library:
    type: Optional[LibraryType] = None
    id: Optional[int] = None
    name: Optional[str] = None
    links: Optional[LibraryLinks] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Library':
        assert isinstance(obj, dict)
        type = from_union([LibraryType, from_none], obj.get("type"))
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([str, from_none], obj.get("name"))
        links = from_union([LibraryLinks.from_dict, from_none], obj.get("links"))
        return Library(type, id, name, links)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(LibraryType, x), from_none], self.type)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([lambda x: to_enum(str, x), from_none], self.name)
        if self.links is not None:
            result["links"] = from_union([lambda x: to_class(LibraryLinks, x), from_none], self.links)
        return result


class AttachmentType(Enum):
    APPLICATION_PDF = "application/pdf"
    TEXT_HTML = "text/html"


@dataclass
class Attachment:
    href: Optional[str] = None
    type: Optional[AlternateType] = None
    attachment_type: Optional[AttachmentType] = None
    attachment_size: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attachment':
        assert isinstance(obj, dict)
        href = from_union([from_str, from_none], obj.get("href"))
        type = from_union([AlternateType, from_none], obj.get("type"))
        attachment_type = from_union([AttachmentType, from_none], obj.get("attachmentType"))
        attachment_size = from_union([from_int, from_none], obj.get("attachmentSize"))
        return Attachment(href, type, attachment_type, attachment_size)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.href is not None:
            result["href"] = from_union([from_str, from_none], self.href)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(AlternateType, x), from_none], self.type)
        if self.attachment_type is not None:
            result["attachmentType"] = from_union([lambda x: to_enum(AttachmentType, x), from_none],
                                                  self.attachment_type)
        if self.attachment_size is not None:
            result["attachmentSize"] = from_union([from_int, from_none], self.attachment_size)
        return result


@dataclass
class TopItemResponseLinks:
    links_self: Optional[Alternate] = None
    alternate: Optional[Alternate] = None
    attachment: Optional[Attachment] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TopItemResponseLinks':
        assert isinstance(obj, dict)
        links_self = from_union([Alternate.from_dict, from_none], obj.get("self"))
        alternate = from_union([Alternate.from_dict, from_none], obj.get("alternate"))
        attachment = from_union([Attachment.from_dict, from_none], obj.get("attachment"))
        return TopItemResponseLinks(links_self, alternate, attachment)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.links_self is not None:
            result["self"] = from_union([lambda x: to_class(Alternate, x), from_none], self.links_self)
        if self.alternate is not None:
            result["alternate"] = from_union([lambda x: to_class(Alternate, x), from_none], self.alternate)
        if self.attachment is not None:
            result["attachment"] = from_union([lambda x: to_class(Attachment, x), from_none], self.attachment)
        return result


@dataclass
class Meta:
    parsed_date: Optional[Union[datetime, int]] = None
    num_children: Optional[int] = None
    creator_summary: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        parsed_date = from_union([from_none, lambda x: from_union([from_datetime, lambda x: int(x)], from_str(x))],
                                 obj.get("parsedDate"))
        num_children = from_union([from_int, from_none], obj.get("numChildren"))
        creator_summary = from_union([from_str, from_none], obj.get("creatorSummary"))
        return Meta(parsed_date, num_children, creator_summary)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.parsed_date is not None:
            result["parsedDate"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                                               lambda x: from_str(
                                                   (lambda x: (lambda x: is_type(datetime, x))(x).isoformat())(x)),
                                               lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))],
                                              self.parsed_date)
        if self.num_children is not None:
            result["numChildren"] = from_union([from_int, from_none], self.num_children)
        if self.creator_summary is not None:
            result["creatorSummary"] = from_union([from_str, from_none], self.creator_summary)
        return result


@dataclass
class TopItemResponseElement:
    key: Optional[str] = None
    version: Optional[int] = None
    library: Optional[Library] = None
    links: Optional[TopItemResponseLinks] = None
    meta: Optional[Meta] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TopItemResponseElement':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        version = from_union([from_int, from_none], obj.get("version"))
        library = from_union([Library.from_dict, from_none], obj.get("library"))
        links = from_union([TopItemResponseLinks.from_dict, from_none], obj.get("links"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return TopItemResponseElement(key, version, library, links, meta, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.version is not None:
            result["version"] = from_union([from_int, from_none], self.version)
        if self.library is not None:
            result["library"] = from_union([lambda x: to_class(Library, x), from_none], self.library)
        if self.links is not None:
            result["links"] = from_union([lambda x: to_class(TopItemResponseLinks, x), from_none], self.links)
        if self.meta is not None:
            result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def top_item_response_from_dict(s: Any) -> List[TopItemResponseElement]:
    return from_list(TopItemResponseElement.from_dict, s)


def top_item_response_to_dict(x: List[TopItemResponseElement]) -> Any:
    return from_list(lambda x: to_class(TopItemResponseElement, x), x)
