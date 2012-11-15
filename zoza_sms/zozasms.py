# encoding=utf-8

import re

from zozaniba.resultat.models import QuestionReponse

from datetime import date, datetime, timedelta


def handler(message):
    """ Zozaniba SMS router """
    def main_zoza_handler(message):
        keyword = 'z'
        commands = {'re': resultat,
                    'q': ask_amswer,
                    'test': z_test,
                    'echo': nut_echo}
        if message.content.lower().startswith('z '):
            for cmd_id, cmd_target in commands.items():
                command = '%s %s' % (keyword, cmd_id)
                if message.content.lower().startswith(command):
                    n, args = re.split(r'^%s\s?' \
                                       % command, \
                                       message.content.lower().strip())
                    return cmd_target(message,
                                      args=args,
                                      sub_cmd=cmd_id,
                                      cmd=command)
        else:
            return False

    if main_zoza_handler(message):
        message.status = message.STATUS_PROCESSED
        message.save()
        return True
    return False


def formatdate(date_, time_=False):
    """ Reçoi un string. return date ou datetime

        exemple: '20120620' or 40 """
    if re.match(r'^\d{8}$', date_):
        if not time_:
            date_now = date.today()
            parsed_date = date(int(date_[0:4]), int(date_[4:6]), \
                           int(date_[6:8]))
        else:
            date_now = datetime.now()
            parsed_date = datetime(int(date_[0:4]), int(date_[4:6]), \
                               int(date_[6:8]), date_now.hour, date_now.minute,
                               date_now.second, date_now.microsecond)
        if date_now < parsed_date:
            raise ValueError(u"[ERREUR] La date est dans le futur.")
        return parsed_date
    else:
        try:
            # date_ est toujour en mois
            print date_
            today = date.today()
            value = int(date_)
            return today - timedelta(30 * value) - timedelta(15)
        except:
            raise ValueError(u"Age unknown: %s" % date_)


def resp_error(message, action):
    message.respond(u"[ERREUR] Impossible de comprendre le SMS pour %s"
                                                               % action)
    return True


def save_error(message, action):
    message.respond(u"[ERREUR] %s" % action)
    return True


def resultat(message, args, sub_cmd, cmd):
    """ Incomming:
            z re num_place
            example: z re 1125
        Outgoing:
            [SUCCES] Vous avez passé """

    try:
        code, msg = message.content.split('z test')
    except:
        msg = ''

    message.respond(u"[SUCCES] %s" % msg)
    return True


def ask_amswer(message, args, sub_cmd, cmd):
    """ Incomming:
            z q num_place
            example: z q bresil a eu combien de coupe du monde"""

    qr = QuestionReponse()
    qr.question = args
    qr.date = datetime.now()
    qr.num_phone = message.identity
    qr.is_amswer = False
    qr.save()
    print qr


def z_test(message, **kwargs):
    try:
        code, msg = message.content.split('z test')
    except:
        msg = ''
    message.respond(u"Received on %(date)s: %(msg)s" \
                    % {'date': datetime.now(), 'msg': msg})
    return True


def nut_echo(message, **kwargs):
    message.respond(kwargs['args'])
    return True
