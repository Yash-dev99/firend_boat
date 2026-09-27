# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from select import select
from django.db import models

class CommentDim(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('PostDim', models.DO_NOTHING, blank=True, null=True)
    comment_type = models.CharField(max_length=20, blank=True, null=True)
    comment_content = models.TextField(blank=True, null=True)
    commented_by = models.ForeignKey('UserDim', models.DO_NOTHING, db_column='commented_by', blank=True, null=True)
    vote = models.BigIntegerField(blank=True, null=True)
    commented_on = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_dim'
        db_table_comment = 'comment dimension, it will have tree structure.'
    
    def __str__(self):
        return str(self.comment_id)


class ConversationDim(models.Model):
    conversation_id = models.BigAutoField(primary_key=True)
    created_by = models.ForeignKey('UserDim', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    created_on = models.TimeField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'conversation_dim'
    
    def __str__(self):
        return str(self.conversation_id)


class ConversationUser(models.Model):
    conversation_user_id = models.BigAutoField(primary_key=True)
    conversation = models.ForeignKey(ConversationDim, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserDim', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'conversation_user'
    
    def __str__(self):
        return str(self.conversation_user_id)



class LoginLog(models.Model):
    login_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserDim', models.DO_NOTHING)
    browser_finger_print = models.TextField(blank=True, null=True)  # This field type is a guess.
    login_ts = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_log'
    
    def __str__(self):
        return str(self.login_id)


class MessagesDim(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    coversation = models.ForeignKey(ConversationDim, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sent_by = models.ForeignKey('UserDim', models.DO_NOTHING, db_column='sent_by', blank=True, null=True)
    sent_on = models.TimeField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'messages_dim'

    def __str__(self):
        return str(self.message_id)


class PostDim(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    up_vote = models.BigIntegerField(blank=True, null=True)
    down_vote = models.BigIntegerField(blank=True, null=True)
    comment_no = models.BigIntegerField(blank=True, null=True)
    posted_by = models.ForeignKey('UserDim', models.DO_NOTHING, db_column='posted_by', blank=True, null=True)
    posted_on = models.TimeField(blank=True, null=True)
    subboat = models.ForeignKey('SubboatDim', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_dim'
        db_table_comment = 'keep all the post here.'

    def __str__(self):
        return str(self.post_id)


class PostVote(models.Model):
    post_vote_id = models.BigAutoField(primary_key=True)
    comment = models.ForeignKey(CommentDim, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserDim', models.DO_NOTHING, blank=True, null=True)
    vote = models.SmallIntegerField(blank=True, null=True)
    updated_ts = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_vote'

    def __str__(self):
        return str(self.post_vote_id)

class SubboatDim(models.Model):
    subboat_id = models.BigIntegerField(primary_key=True)
    subboat_name = models.CharField(unique=True, max_length=25, blank=True, null=True)
    owner = models.ForeignKey('UserDim', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.BinaryField(blank=True, null=True)
    cover_pic = models.BinaryField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    update_ts = models.TimeField(blank=True, null=True)
    created_ts = models.TimeField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'subboat_dim'
        db_table_comment = 'A group page for people to connect and post'
    
    def __str__(self):
        return "b/"+self.subboat_name


class SubboatJoin(models.Model):
    subboat_join_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserDim', models.DO_NOTHING, blank=True, null=True)
    subboat = models.ForeignKey(SubboatDim, models.DO_NOTHING, blank=True, null=True)
    user_subboat_type = models.CharField(max_length=20, blank=True, null=True)
    joined_at = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subboat_join'

    def __str__(self):
        return  f"{self.subboat.subboat_name}/{self.user.user_name}"


class UserDetail(models.Model):
    user_detail_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserDim', models.DO_NOTHING)
    first_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    middle_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_ts = models.TimeField(blank=True, null=True)
    updated_ts = models.TimeField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user_details'
        db_table_comment = 'details of users'

    def __str__(self):
        return "u/"+self.user.user_name


class UserDim(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.TextField(unique=True)  # This field type is a guess.
    status = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.BinaryField(blank=True, null=True)
    cover_pic = models.BinaryField(blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user_dim'
        db_table_comment = 'user dimension table'

    def __str__(self):
        return self.user_name


class UserPassword(models.Model):
    password_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(UserDim, models.DO_NOTHING, blank=True, null=True)
    password_hash = models.TextField()
    salt = models.TextField(blank=True, null=True)
    created_ts = models.TimeField(blank=True, null=True)
    update_ts = models.TimeField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user_password'
        db_table_comment = 'keep your password secure'

    def __str__(self):
        return self.user_name