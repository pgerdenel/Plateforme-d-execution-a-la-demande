is_beginning = False;
is_repo_ready = False;
is_container_ready = False;
is_tache_ready = False;
is_projet_ended = False;
all_task_received = False;

def get_is_beginning() :
    return is_beginning

def set_is_beginning(state) :
    is_beginning = state