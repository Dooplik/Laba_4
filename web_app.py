import datetime
import fastapi
import model

api_router = fastapi.APIRouter()
id_list = [1]


class Note:
    def __init__(self, note_id, text, created_time, updated_time):
        self.id = note_id
        self.text = text
        self.created_time = created_time
        self.updated_time = updated_time

    def to_string(self):
        return " ".join([str(self.id), str(self.text), str(self.created_time), str(self.updated_time)])


def update_note_text(string, text):
    args = string.split(" ")
    print(len(args))
    if len(args) != 6:
        return None
    return Note(args[0], text, args[2] + " " + args[3], datetime.datetime.now())


def token_validation(line):
    file = open("tokens", "r").read().split("\n")
    if str(line) in file:
        return True
    else:
        return False


@api_router.post("/create", response_model=model.Create)
def create_note(text: str, token: str):
    global id_list
    file = open("notes", "r").read().split("\n")
    if len(id_list) <= 1:
        id_list.append(0)
    else:
        id_list = [int(file[i][0]) for i in range(len(file))]
    if token_validation(token):
        id_list.append(id_list[-1] + 1)
        note = Note(id_list[-1], text, datetime.datetime.now(), datetime.datetime.now())
        file = open("notes", "a")
        file.write(f"\n{note.to_string()}")
        return model.Create(
            id=note.id
        )
    else:
        return model.GetText(
            id=-1,
            text="ERROR"
        )


@api_router.delete("/delete", response_model=model.Delete)
def delete_note(ID: int, token: str):
    if token_validation(token):
        file = open("notes", "r")
        note_list = file.read().split("\n")
        for i in range(len(note_list)):
            if note_list[i][0] == str(ID):
                note_list.pop(i)
                break
        file = open("notes", "w")
        file.write("\n".join(note_list))
        return model.Delete(
            removed_id=ID
        )
    else:
        return model.GetText(
            id=-1,
            text="ERROR"
        )


@api_router.get("/getList", response_model=model.GetList)
def get_notes_list(token: str):
    if token_validation(token):
        file = open("notes", "r")
        note_list = file.read().split("\n")
        list_of_id = [note[0] for note in note_list]
        return model.GetList(
            notes_list={i: list_of_id[i] for i in range(len(list_of_id))}
        )
    else:
        return model.GetText(
            id=-1,
            text="ERROR"
        )


@api_router.get("/getInfo", response_model=model.GetInfo)
def get_note_info(ID: int, token: str):
    if token_validation(token):
        file = open("notes", "r")
        note_list = file.read().split("\n")
        for i in range(len(note_list)):
            if note_list[i][0] == str(ID):
                return model.GetInfo(
                    created_at=note_list[i].split(" ")[2] + " " + note_list[i].split(" ")[3],
                    updated_at=note_list[i].split(" ")[4] + " " + note_list[i].split(" ")[5],
                )
        return model.GetText(
            id=-1,
            text="ERROR"
        )
    else:
        return model.GetText(
            id=-1,
            text="ERROR"
        )


@api_router.patch("/update", response_model=model.Update)
def update_note(ID: int, text: str, token: str):
    if token_validation(token):
        file = open("notes", "r")
        note_list = file.read().split("\n")
        for i in range(len(note_list)):
            if note_list[i][0] == str(ID):
                note_list[i] = update_note_text(note_list[i], text).to_string()
        file = open("notes", "w")
        file.write("\n".join(note_list))
        return model.Update(
            id=ID,
            text=text
        )
    else:
        return model.GetText(
            id=-1,
            text="ERROR"
        )


@api_router.get("/getText", response_model=model.GetText)
def get_note_for_id(ID: int, token: str):
    if token_validation(token):
        file = open("notes", "r")
        note_list = file.read().split("\n")
        for i in range(len(note_list)):
            if note_list[i][0] == str(ID):
                return model.GetText(
                    id=ID,
                    text=note_list[i].split(" ")[1]
                )
            return model.GetText(
                    id=-1,
                    text="ERROR"
                )

    else:
        return model.GetText(
            id=-1,
            text="ERROR"
        )
