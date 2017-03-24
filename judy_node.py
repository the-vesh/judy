class TreeNode:
    node_count = 0

    def __init__(self, parent, left_child, right_child):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        TreeNode.node_count += 1

    def get_number_of_nodes(self):
        return TreeNode.node_count

class QuestionNode(TreeNode):
    question_count = 0

    def __init__(self, parent, question, no_child, yes_child):
        self.parent = parent
        self.question = question
        self.no_child = no_child
        self.yes_child = yes_child
        QuestionNode.question_count += 1

    def get_number_of_questions(self):
        return QuestionNode.question_count

class ItemNode(TreeNode):
    item_count = 0

    def __init__(self, item_name, bitmap, parent):
        self.item_name = item_name
        self.bitmap = bitmap
        self.parent = parent
        ItemNode.question_count += 1

    def get_number_of_items(self):
        return ItemNode.item_count
