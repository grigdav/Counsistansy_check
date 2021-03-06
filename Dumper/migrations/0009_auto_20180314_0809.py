# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-14 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dumper', '0008_auto_20180314_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_alignttibundwultrigsinr',
            field=models.CharField(blank=True, db_column='field_enodeb_alignTtiBundWUlTrigSinr', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_altnasbackto',
            field=models.CharField(blank=True, db_column='field_enodeb_altNasBackTo', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_biasthpwifimobility',
            field=models.CharField(blank=True, db_column='field_enodeb_biasThpWifiMobility', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_caawaremfbiintracellho',
            field=models.CharField(blank=True, db_column='field_enodeb_caAwareMfbiIntraCellHo', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_checkemergencysoftlock',
            field=models.CharField(blank=True, db_column='field_enodeb_checkEmergencySoftLock', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_combcellsectorselectthreshrx',
            field=models.CharField(blank=True, db_column='field_enodeb_combCellSectorSelectThreshRx', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_combcellsectorselectthreshtx',
            field=models.CharField(blank=True, db_column='field_enodeb_combCellSectorSelectThreshTx', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_csfbmeasfromidlemode',
            field=models.CharField(blank=True, db_column='field_enodeb_csfbMeasFromIdleMode', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_csfbuseregisteredlai',
            field=models.CharField(blank=True, db_column='field_enodeb_csfbUseRegisteredLai', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_csmminhighhitthreshold',
            field=models.CharField(blank=True, db_column='field_enodeb_csmMinHighHitThreshold', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_dlmaxwaitingtimeglobal',
            field=models.CharField(blank=True, db_column='field_enodeb_dlMaxWaitingTimeGlobal', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_dnslookupontai',
            field=models.CharField(blank=True, db_column='field_enodeb_dnsLookupOnTai', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_dnslookuptimer',
            field=models.CharField(blank=True, db_column='field_enodeb_dnsLookupTimer', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_dnsselections1x2ref',
            field=models.CharField(blank=True, db_column='field_enodeb_dnsSelectionS1X2Ref', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_dscplabel',
            field=models.CharField(blank=True, db_column='field_enodeb_dscpLabel', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_enabledultrigmeas',
            field=models.CharField(blank=True, db_column='field_enodeb_enabledUlTrigMeas', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_enbid',
            field=models.CharField(blank=True, db_column='field_enodeb_eNBId', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_enodebplmnid',
            field=models.CharField(blank=True, db_column='field_enodeb_eNodeBPlmnId', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_eranvlanportref',
            field=models.CharField(blank=True, db_column='field_enodeb_eranVlanPortRef', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_extendedwaittimenb',
            field=models.CharField(blank=True, db_column='field_enodeb_extendedWaitTimeNb', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_forcedsitunnelingactive',
            field=models.CharField(blank=True, db_column='field_enodeb_forcedSiTunnelingActive', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_gtpuerrorindicationdscp',
            field=models.CharField(blank=True, db_column='field_enodeb_gtpuErrorIndicationDscp', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_inactivitysupervisiontimernb',
            field=models.CharField(blank=True, db_column='field_enodeb_inactivitySupervisionTimerNb', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_inactivitysupervisiontimernb_1',
            field=models.CharField(blank=True, db_column='field_enodeb_inactivitySupervisionTimerNb_1', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_inactivitysupervisiontimernb_2',
            field=models.CharField(blank=True, db_column='field_enodeb_inactivitySupervisionTimerNb_2', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_initpreschedulingenable',
            field=models.CharField(blank=True, db_column='field_enodeb_initPreschedulingEnable', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_interenbcatunneldscp',
            field=models.CharField(blank=True, db_column='field_enodeb_interEnbCaTunnelDscp', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_interenbulcomptunneldscp',
            field=models.CharField(blank=True, db_column='field_enodeb_interEnbUlCompTunnelDscp', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_ipsecepaddressref',
            field=models.CharField(blank=True, db_column='field_enodeb_ipsecEpAddressRef', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_liccapdistrmethod',
            field=models.CharField(blank=True, db_column='field_enodeb_licCapDistrMethod', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_licconnecteduserspercentileconf',
            field=models.CharField(blank=True, db_column='field_enodeb_licConnectedUsersPercentileConf', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_licdlbbpercentileconf',
            field=models.CharField(blank=True, db_column='field_enodeb_licDlBbPercentileConf', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_licdlprbpercentileconf',
            field=models.CharField(blank=True, db_column='field_enodeb_licDlPrbPercentileConf', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_liculbbpercentileconf',
            field=models.CharField(blank=True, db_column='field_enodeb_licUlBbPercentileConf', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_liculprbpercentileconf',
            field=models.CharField(blank=True, db_column='field_enodeb_licUlPrbPercentileConf', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_maxnrofinterenbulcomplbm',
            field=models.CharField(blank=True, db_column='field_enodeb_maxNrOfInterEnbUlCompLbm', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_maxrandc',
            field=models.CharField(blank=True, db_column='field_enodeb_maxRandc', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_measuringecgiwithagactive',
            field=models.CharField(blank=True, db_column='field_enodeb_measuringEcgiWithAgActive', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_mfbisupport',
            field=models.CharField(blank=True, db_column='field_enodeb_mfbiSupport', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_mfbisupportpolicy',
            field=models.CharField(blank=True, db_column='field_enodeb_mfbiSupportPolicy', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_minrandc',
            field=models.CharField(blank=True, db_column='field_enodeb_minRandc', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_mtrrewithoutneighboractive',
            field=models.CharField(blank=True, db_column='field_enodeb_mtRreWithoutNeighborActive', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_plmnbordernode',
            field=models.CharField(blank=True, db_column='field_enodeb_plmnBorderNode', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_prioritizeadditionalbands',
            field=models.CharField(blank=True, db_column='field_enodeb_prioritizeAdditionalBands', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_pwspersistentstorage',
            field=models.CharField(blank=True, db_column='field_enodeb_pwsPersistentStorage', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_randupdateinterval',
            field=models.CharField(blank=True, db_column='field_enodeb_randUpdateInterval', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_release',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_releaseinactiveuesinacttime',
            field=models.CharField(blank=True, db_column='field_enodeb_releaseInactiveUesInactTime', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_releaseinactiveuesmploadlevel',
            field=models.CharField(blank=True, db_column='field_enodeb_releaseInactiveUesMpLoadLevel', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_rrcconnreestactive',
            field=models.CharField(blank=True, db_column='field_enodeb_rrcConnReestActive', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_s1gtpuechodscp',
            field=models.CharField(blank=True, db_column='field_enodeb_s1GtpuEchoDscp', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_s1gtpuechoenable',
            field=models.CharField(blank=True, db_column='field_enodeb_s1GtpuEchoEnable', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_s1gtpuechofailureaction',
            field=models.CharField(blank=True, db_column='field_enodeb_s1GtpuEchoFailureAction', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_s1hodirdatapathavail',
            field=models.CharField(blank=True, db_column='field_enodeb_s1HODirDataPathAvail', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_s1retrytimer',
            field=models.CharField(blank=True, db_column='field_enodeb_s1RetryTimer', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_sctpref',
            field=models.CharField(blank=True, db_column='field_enodeb_sctpRef', max_length=191, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_sctpx2ref',
            field=models.CharField(blank=True, db_column='field_enodeb_sctpX2Ref', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_softlockrwrwaittimerinternal',
            field=models.CharField(blank=True, db_column='field_enodeb_softLockRwRWaitTimerInternal', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_softlockrwrwaittimeroperator',
            field=models.CharField(blank=True, db_column='field_enodeb_softLockRwRWaitTimerOperator', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_tddvoipdrxprofileid',
            field=models.CharField(blank=True, db_column='field_enodeb_tddVoipDrxProfileId', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timeandphasesynchalignment',
            field=models.CharField(blank=True, db_column='field_enodeb_timeAndPhaseSynchAlignment', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timeandphasesynchcritical',
            field=models.CharField(blank=True, db_column='field_enodeb_timeAndPhaseSynchCritical', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationcdma2000',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationCdma2000', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationedrx',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationEdrx', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationienbca',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationIeNbCa', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationmbms',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationMbms', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationotdoa',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationOtdoa', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationsib16',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationSib16', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd1',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd1', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd2',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd2', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd3',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd3', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd4',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd4', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd5',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd5', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd6',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd6', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdeviationtdd7',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviationTdd7', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_timephasemaxdevienbulcomp',
            field=models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDevIeNBUlComp', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_toutgoinghoexeccdma1xrtt',
            field=models.CharField(blank=True, db_column='field_enodeb_tOutgoingHoExecCdma1xRtt', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_trelocoverall',
            field=models.CharField(blank=True, db_column='field_enodeb_tRelocOverall', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_ts1hocanceltimer_field',
            field=models.CharField(blank=True, db_column="field_enodeb_tS1HoCancelTimer'", max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_ulmaxwaitingtimeglobal',
            field=models.CharField(blank=True, db_column='field_enodeb_ulMaxWaitingTimeGlobal', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_ulschedulerdynamicbwallocationenabled',
            field=models.CharField(blank=True, db_column='field_enodeb_ulSchedulerDynamicBWAllocationEnabled', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_upipaddressref',
            field=models.CharField(blank=True, db_column='field_enodeb_upIpAddressRef', max_length=191, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_upx2ipaddressref',
            field=models.CharField(blank=True, db_column='field_enodeb_upX2IpAddressRef', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_usebandprioritiesinscelleval',
            field=models.CharField(blank=True, db_column='field_enodeb_useBandPrioritiesInSCellEval', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_usebandprioritiesinsib1',
            field=models.CharField(blank=True, db_column='field_enodeb_useBandPrioritiesInSib1', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_userlabel',
            field=models.CharField(blank=True, db_column='field_enodeb_userLabel', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2blacklist',
            field=models.CharField(blank=True, db_column='field_enodeb_x2BlackList', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2gtpuechodscp',
            field=models.CharField(blank=True, db_column='field_enodeb_x2GtpuEchoDscp', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2gtpuechoenable',
            field=models.CharField(blank=True, db_column='field_enodeb_x2GtpuEchoEnable', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2ipaddrvias1active',
            field=models.CharField(blank=True, db_column='field_enodeb_x2IpAddrViaS1Active', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2retrytimermaxauto',
            field=models.CharField(blank=True, db_column='field_enodeb_x2retryTimerMaxAuto', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2retrytimerstart',
            field=models.CharField(blank=True, db_column='field_enodeb_x2retryTimerStart', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2setuptwowayrelations',
            field=models.CharField(blank=True, db_column='field_enodeb_x2SetupTwoWayRelations', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_x2whitelist',
            field=models.CharField(blank=True, db_column='field_enodeb_x2WhiteList', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary1',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary1', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary10',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary10', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary11',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary11', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary12',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary12', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary13',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary13', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary16',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary16', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary18',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary18', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary2',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary2', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary21',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary21', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary22',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary22', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary23',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary23', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary24',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary24', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary25',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary25', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary26',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary26', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary28',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary28', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary3',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary3', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary32',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary32', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary33',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary33', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary34',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary34', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary35',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary35', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary36',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary36', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary37',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary37', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary39',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary39', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary40',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary40', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary41',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary41', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary42',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary42', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary43',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary43', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary47',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary47', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary48',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary48', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary49',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary49', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary5',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary5', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary50',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary50', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary51',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary51', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary52',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary52', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary53',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary53', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary54',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary54', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary55',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary55', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary56',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary56', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary57',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary57', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary58',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary58', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary6',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary6', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary7',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary7', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary8',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary8', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='enodebfunction',
            name='field_enodeb_zzztemporary9',
            field=models.CharField(blank=True, db_column='field_enodeb_zzzTemporary9', max_length=45, null=True),
        ),
    ]
